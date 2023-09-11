"""________________________________Libraries________________________________"""

from termcolor import colored
import matplotlib.pyplot as plt   # for plotting
import numpy as np   # matrices, math
from scipy.integrate import solve_ivp   # differential equation solver
from scipy.signal import argrelmin   # loc min finding
import time   # runtime measurement
from numba import njit   # Just In Time compiler
from numba.types import unicode_type, float64, float32, int64, int32   # JIT types
from func_timeout import func_timeout, FunctionTimedOut   # for timeout
import os    # file management
import importlib   # for reloading your own files

# my own files:
try:
    import parameters as par   # numeric constants and coefficents
    importlib.reload(par)   # reload changes you made
    print(f'model: {par.model}')
except:
    print(print(colored('Error, \'parameters.py\' not found','red')))

# dot.notation access to dictionary attributes
# instead of dictionary['key'] you can use dictionary.key
class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
    

"""________________________________Before the simulation________________________________"""
par.R_v=par.R_g/(2.0*par.W[par.index['H']]+par.W[par.index['O']])*1000.0 # [Pa]
for j in range(3*len(par.PlogIndexes)):
    par.Plog[j][0] = par.Plog[j][0] * 1.0e5 # [bar] -> [Pa]

@njit(float64(float64))
def VapourPressure(T): # [K]
    T -= 273.15 # [°C]
    return 611.21 * np.exp( (18.678 - T / 234.5) * (T / (257.14 + T)) ) # [Pa]

@njit(float64(float64))
def Viscosity(T): # [K], pressure dependence is neglected
    return 1.856e-14 * np.exp(4209.0/T + 0.04527*T - 3.376e-5*T**2) # [Pa*s]

def InitialCondition(cpar, evaporation=False):
    if not 'P_v' in cpar:
        cpar.P_v = VapourPressure(T=cpar.T_inf) # [Pa]
    if not 'mu_L' in cpar:
        cpar.mu_L = Viscosity(T=cpar.T_inf) # [Pa]
    if not 'c_L' in cpar:
        cpar.c_L = par.c_L # [m/s]
    if type(cpar.gases) != list:
        cpar.gases = [cpar.gases]
    if type(cpar.fractions) != list:
        cpar.fractions = [cpar.fractions]
    if sum(cpar.fractions) != 1.0:
        print(print(colored('Warning, in InitialCondition(), sum of cpar.fractions isn\'t 1.','yellow')));print(cpar.fractions)
    IC = np.zeros((par.K+4), dtype=np.float64)
    R_0 = cpar.ratio * cpar.R_E
    
    # Equilibrium state
    p_E = cpar.P_amb + 2.0 * cpar.surfactant * par.sigma / cpar.R_E # [Pa]
    V_E = 4.0 / 3.0 * cpar.R_E**3 * np.pi # [m^3]
    p_gas = p_E - cpar.P_v if evaporation else p_E
    negativepressure_error = False
    if p_gas < 0.0:
        print('Error! The pressure of the gas is negative!')
        negativepressure_error = True
    n_gas = p_gas * V_E / (par.R_g * cpar.T_inf) # [mol]
    
    # Isotermic expansion
    V_0 = 4.0 / 3.0 * R_0**3 * np.pi    # [m^3]
    n_H2O = cpar.P_v * V_0 / (par.R_g * cpar.T_inf) if evaporation else 0.0 # [mol]
    c_H2O = n_H2O / V_0    # [mol/m^3]
    c_gas = n_gas / V_0    # [mol/m^3]

    # Initial conditions
    IC[0] = R_0   # R_0 [m]
    IC[1] = 0.0    # dRdt_0 [m/s]
    IC[2] = cpar.T_inf   # T_0 [K]
    IC[3 + par.index['H2O']] = c_H2O * 1.0e-6    # [mol/cm^3]
    for index, fraction in zip(cpar.gases, cpar.fractions):
        IC[3 + index] = fraction * c_gas * 1.0e-6    # [mol/cm^3]
    IC[3 + par.K] = 0.0 #dissipated acoustic energy [J]
    return IC,negativepressure_error


def Work(cpar, evaporation=False):
    if not 'P_v' in cpar:
        cpar.P_v = VapourPressure(T=cpar.T_inf) # [Pa]
    if not 'mu_L' in cpar:
        cpar.mu_L = Viscosity(T=cpar.T_inf) # [Pa]
    R_0 = cpar.ratio * cpar.R_E # [m]
    V_E = 4.0 / 3.0 * cpar.R_E**3 * np.pi    # [m^3]
    V_0 = 4.0 / 3.0 * R_0**3 * np.pi  # [m^3]
    
    p_E = cpar.P_amb + 2 * cpar.surfactant * par.sigma / cpar.R_E # [Pa]
    p_gas = p_E - cpar.P_v if evaporation else p_E # [Pa]
    n_gas = p_gas * V_E / (par.R_g * cpar.T_inf) # [mol]
    
    W_gas0 = -(cpar.P_v * V_0 + n_gas * par.R_g * cpar.T_inf * np.log(V_0)) if evaporation else -(n_gas * par.R_g * cpar.T_inf * np.log(V_0))
    W_gasE = -(cpar.P_v * V_E + n_gas * par.R_g * cpar.T_inf * np.log(V_E)) if evaporation else -(n_gas * par.R_g * cpar.T_inf * np.log(V_E))
    W_gas = W_gas0 - W_gasE # [J]
    
    W_surface_tension = par.sigma * cpar.surfactant *  4.0 * np.pi * (R_0**2 - cpar.R_E**2) # [J]
    W_flow = cpar.P_amb * 4.0 / 3.0 * np.pi * (R_0**3.0 - cpar.R_E**3.0) # [J]
    return W_gas + W_surface_tension + W_flow    # [J]


"""________________________________Pressures________________________________"""

@njit(float64[:](float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64))
def Pressure(t, R, R_dot, T, T_dot, M, sum_omega_dot, P_amb, mu_L, surfactant, freq1, freq2, pA1, pA2, theta_phase):
    p_Inf = P_amb + pA1*np.sin(2.0*np.pi*freq1*t) + pA2*np.sin(2.0*np.pi*freq2*t+theta_phase) 
    p_Inf_dot = pA1*2.0*np.pi*freq1*np.cos(2.0*np.pi*freq1*t) + pA2*2.0*np.pi*freq2*np.cos(2.0*np.pi*freq2*t+theta_phase)
    p = 0.1 * M * par.R_erg * T
    p_dot = p * (sum_omega_dot / M + T_dot / T - 3.0 * R_dot/R)
    p_L = p - (2.0 * surfactant * par.sigma + 4.0 * mu_L * R_dot) / R
    p_L_dot = p_dot + (-2.0 * surfactant * par.sigma * R_dot + 4.0 * mu_L * R_dot ** 2) / (R ** 2)
    delta = (p_L - p_Inf) / par.rho_L
    delta_dot = (p_L_dot - p_Inf_dot) / par.rho_L
    return np.array([delta, delta_dot, p_dot])


"""________________________________NASA polynomials________________________________"""

# Returns the right set of NASA coefficents
@njit(float64[:](int32, float64))
def getCoeffs(k, T):
    a = np.zeros((7), dtype=np.float64)
    if T <= par.TempRange[k][2]: # T <= T_mid
        a = par.a_low[k]
    else:  # T_mid < T
        a = par.a_high[k]
    return a


# returns molar heat capacities, enthalpies and entropies
@njit(float64[:, :](float64[:], float64))
def Thermodynamic(c, T):
    ret = np.zeros((4, par.K), dtype=np.float64)   # [C_p, H, S, C_v]
    exponent = np.array([1, 2, 3, 4, 5])
    for k in range(par.K):
    # get coefficients for T
        a = getCoeffs(k, T)
            
     # calculate
        T_vec = T ** (exponent-1)    # [1, T, T^2, T^3, T^4]
        # Molar heat capacities at constant pressure (isobaric) [erg/mol/K]
        ret[0][k] = par.R_erg * np.sum(a[:par.N] * T_vec)
        # Enthalpies [erg/mol]
        ret[1][k] = par.R_erg * ( T * np.sum(a[:par.N] * T_vec / exponent) + a[par.N])
        # Entropies [erg/mol/K]
        ret[2][k] = par.R_erg * (a[0] * np.log(T) + np.sum(a[1:par.N] * T_vec[1:] / (exponent[1:]-1)) + a[par.N+1])
    # Molar heat capacities at constant volume (isochoric) [erg/mol/K]
    ret[3] = ret[0] - par.R_erg 
    return ret


"""________________________________Evaporation________________________________"""

@njit(float64[:](float64, float64, float64, float64, float64, float64))
def Evaporation(M, T, X_H2O, alfa_M, T_inf, P_v):
# condensation and evaporation
    p = 0.1 * M * par.R_erg * T
    p_H2O = X_H2O * p
    n_eva_dot = 1.0e3 * alfa_M * P_v / (par.W[par.indexOfWater] * np.sqrt(2.0 * np.pi * par.R_v * T_inf))
    n_con_dot = 1.0e3 * alfa_M * p_H2O / (par.W[par.indexOfWater] * np.sqrt(2.0 * np.pi * par.R_v * T))
    n_net_dot = n_eva_dot - n_con_dot
# Molar heat capacity of water at constant volume (isochoric) [erg/mol/K]
    exponent = np.array([1, 2, 3, 4, 5])
    a = getCoeffs(par.indexOfWater, T)
    T_vec = T ** (exponent-1)    # [1, T, T^2, T^3, T^4]
    C_v = par.R_erg * (np.sum(a[:par.N] * T_vec) - 1.0)
    
    a = getCoeffs(par.indexOfWater, T_inf)
    T_vec = T_inf ** (exponent-1)    # [1, T, T^2, T^3, T^4]
    C_v_inf = par.R_erg * (np.sum(a[:par.N] * T_vec) - 1.0)
# Evaporation energy
    e_eva = C_v_inf * T_inf * 1e-7   # [J/mol]
    e_con = C_v * T * 1e-7
    evap_energy = n_eva_dot * e_eva - n_con_dot * e_con    # [W/m^2]
    
    return np.array([n_net_dot, evap_energy])


"""________________________________Reaction rates________________________________"""

@njit(float64[:](float64, float64[:], float64))
def ForwardRate(T, M_eff, M):
# Reaction rate
    k_forward = par.A * T ** par.b * np.exp(-par.E / (par.R_cal * T))
    
# Pressure dependent reactions
    LindemannIndex=0
    TroeIndex=0
    SRIIndex=0
    
    for j, i in enumerate(par.PressureDependentIndexes):    # i is the number of reaction, j is the index of i's place in par.PressureDependentIndexes
        k_inf = k_forward[i]    # par.A[i] * T ** par.b[i] * np.exp(-par.E[i] / (par.R_cal * T))
        k_0 = par.ReacConst[j][0] * T ** par.ReacConst[j][1] * np.exp(-par.ReacConst[j][2] / (par.R_cal * T))
        P_r = k_0 / k_inf * M_eff[i]
        logP_r = np.log10(P_r)
        
         # Lindemann formalism
        if i in par.LindemannIndexes:
            F = 1.0
            LindemannIndex += 1

    # Troe formalism
        elif i in par.TroeIndexes:
            F_cent = (1.0 - par.Troe[TroeIndex][0]) * np.exp(-T / par.Troe[TroeIndex][1]) + par.Troe[TroeIndex][0] * np.exp(-T / par.Troe[TroeIndex][2]) + np.exp(-par.Troe[TroeIndex][3] / T)
            logF_cent = np.log10(F_cent)
            c2 = -0.4 - 0.67 * logF_cent
            n = 0.75 - 1.27 * logF_cent
            d = 0.14
            logP_r = np.log10(P_r)
            logF = 1.0 / (1.0 + ((logP_r + c2) / (n - d * (logP_r + c2))) ** 2) * logF_cent
            F = 10.0 ** logF
            TroeIndex += 1
        
        # SRI formalism
        elif i in par.SRIIndexes: 
            X = 1.0 / (1.0 + np.log10(P_r)**2)
            F = par.SRI[SRIIndex][3] * (par.SRI[SRIIndex][0] * np.exp(-par.SRI[SRIIndex][1] / T) + np.exp(-T / par.SRI[SRIIndex][2]))**X * T ** par.SRI[SRIIndex][4]
            SRIIndex += 1
        else:
            print('Error, the pressure-dependent reaction cannot be groupped in any type of pressure-dependent reactions!','red')
      # Pressure dependent reactions END
    
        k_forward[i] = k_inf * P_r / (1.0 + P_r) * F

  # PLOG reactions
    if par.PlogCount > 0:
        p = 0.1 * M * par.R_erg * T
    for j, i in enumerate(par.PlogIndexes):
        #if p < par.Plog[3*j][0]:
        #    k_forward[i] = par.Plog[3*j][1] * T ** par.Plog[3*j][2] * np.exp(-par.Plog[3*j][3] / (par.R_cal * T))
        #elif p < par.Plog[3*j+1][0]:
        if p < par.Plog[3*j+1][0]:
            k_1 = par.Plog[3*j][1] * T ** par.Plog[3*j][2] * np.exp(-par.Plog[3*j][3] / (par.R_cal * T))
            k_2 = par.Plog[3*j+1][1] * T ** par.Plog[3*j+1][2] * np.exp(-par.Plog[3*j+1][3] / (par.R_cal * T))
            ln_k = np.log(k_1) + (np.log(p) - np.log(par.Plog[3*j][0])) / (np.log(par.Plog[3*j+1][0]) - np.log(par.Plog[3*j][0])) * (np.log(k_2) - np.log(k_1))
            k_forward[i] = np.exp(ln_k)
        #elif p < par.Plog[3*j+2][0]:
        else:
            k_2 = par.Plog[3*j+1][1] * T ** par.Plog[3*j+1][2] * np.exp(-par.Plog[3*j+1][3] / (par.R_cal * T))
            k_3 = par.Plog[3*j+2][1] * T ** par.Plog[3*j+2][2] * np.exp(-par.Plog[3*j+2][3] / (par.R_cal * T))
            ln_k = np.log(k_2) + (np.log(p) - np.log(par.Plog[3*j+1][0])) / (np.log(par.Plog[3*j+2][0]) - np.log(par.Plog[3*j+1][0])) * (np.log(k_3) - np.log(k_2))
            k_forward[i] = np.exp(ln_k)
        #else:
        #    k_forward[i] = par.Plog[3*j+2][1] * T ** par.Plog[3*j+2][2] * np.exp(-par.Plog[3*j+2][3] / (par.R_cal * T))  
    return k_forward


@njit(float64[:](float64[:], float64[:], float64[:], float64, float64))
def BackwardRate(k_forward, S, H, T, P_amb):
    DeltaS = np.sum(par.nu * S, axis=1)
    DeltaH = np.sum(par.nu * H, axis=1)
    K_p = np.exp(DeltaS / par.R_erg - DeltaH / (par.R_erg * T))
    K_c = K_p * (P_amb * 10.0 / (par.R_erg * T)) ** np.sum(par.nu, axis=1)
    k_backward = k_forward / K_c
    for i in par.IrreversibleIndexes:
        k_backward[i] = 0.0
    return k_backward


@njit(float64[:](float64, float64[:], float64[:], float64[:], float64, float64))
def ProductionRate(T, H, S, c, P_amb, M):
# Third body correction factors
    M_eff = np.sum(c) * np.ones((par.I), dtype = np.float64)    # effective total concentration of the third-body 
    for j, i in enumerate(par.ThirdBodyIndexes):
        M_eff[i] = np.sum(par.alfa[j] * c) 
# Forward and backward rates
    k_forward = ForwardRate(T=T, M_eff=M_eff, M=M)
    k_backward = BackwardRate(k_forward=k_forward, S=S, H=H, T=T, P_amb=P_amb)

# Net rates
    q = np.zeros((par.I), dtype = np.float64)
    for i in range(par.I):
        q[i] = k_forward[i] * np.prod(c ** par.nu_forward[i]) - k_backward[i] * np.prod(c ** par.nu_backward[i])
# Third body reactions
    for j, i in enumerate(par.ThirdBodyIndexes):    # i is the number of reaction, j is the index of i in par.ThirdBodyIndexes
        if i not in par.PressureDependentIndexes:
            q[i] *= M_eff[i]
# Production rates
    omega_dot = np.zeros((par.K), dtype=np.float64)
    for k in range(par.K):
        omega_dot[k] = np.sum(par.nu[:, k] * q)
    
    return omega_dot


"""________________________________Differential equation________________________________"""

enable_heat_transfer = True
enable_evaporation = False
enable_reactions = True
print('Enable heat transfer: '+str(enable_heat_transfer)+', enable evaporation: '+str(enable_evaporation)+', enable reactions: '+str(enable_reactions))

@njit(float64[:](float64, float64[:], float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64, float64))
def f(t, x, P_amb, alfa_M, T_inf, surfactant, P_v, mu_L, freq1, freq2, pA1, pA2, theta_phase, c_L):   
    R = x[0]      # bubble radius [m]
    R_dot = x[1]  # [m/s]
    T = x[2]      # temperature [K]
    c = x[3:-1]     # molar concentration [mol/cm^3]
    M = np.sum(c) # sum of concentration
    X = c / M     # mole fraction [-]
    dxdt = np.zeros(x.shape, dtype = np.float64)
    
# d/dt R
    dxdt[0] = R_dot
# Evaporation
    n_net_dot = 0.0  
    evap_energy = 0.0
    if enable_evaporation:
        n_net_dot, evap_energy = Evaporation(M=M, T=T, X_H2O=X[par.indexOfWater], alfa_M=alfa_M, T_inf=T_inf, P_v=P_v)
# Thermodynamics
    [C_p, H, S, C_v] = Thermodynamic(c=c, T=T)
    W_avg = np.sum(X * par.W)
    rho_avg = W_avg * M # or np.sum(c * par.W)
    C_p_avg = np.sum(X * C_p)
    C_v_avg = np.sum(X * C_v)

    lambda_avg = np.sum(X * par.lambdas)
    chi_avg = 10.0 * lambda_avg * W_avg / (C_p_avg * rho_avg)
    l_th = np.inf
    if R_dot != 0.0:
        l_th = np.sqrt(R * chi_avg / abs(R_dot))
    l_th = min(l_th, R / np.pi)
    Q_th_dot = 0.0
    if enable_heat_transfer:
        Q_th_dot = lambda_avg * (T_inf - T) / l_th
# d/dt c
    omega_dot = np.zeros((par.K), dtype = np.float64)
    if enable_reactions:
        omega_dot = ProductionRate(T=T, H=H, S=S, c=c, P_amb=P_amb, M=M)
    c_dot = omega_dot - c * 3.0 * R_dot / R
    c_dot[par.indexOfWater] += 1.0e-6 * n_net_dot * 3.0 / R    # water evaporation
    dxdt[3:-1] = c_dot
# d/dt T
    Q_r_dot = -np.sum(H * omega_dot) + np.sum(omega_dot) * par.R_erg * T
    p = 0.1 * M * par.R_erg * T
    T_dot = (Q_r_dot + 30.0 / R * (-p * R_dot + Q_th_dot + evap_energy)) / (M * C_v_avg)
    dxdt[2] = T_dot
# d/dt R_dot
    [delta, delta_dot, p_dot] = Pressure(t=t,
        R=R, R_dot=R_dot, T=T, T_dot=T_dot,
        M=M, sum_omega_dot=np.sum(omega_dot),
        P_amb=P_amb, mu_L=mu_L, surfactant=surfactant,
        freq1=freq1, freq2=freq2, pA1=pA1, pA2=pA2, theta_phase=theta_phase
    )   # delta = (p_L-P_amb) / rho_L
    
    Nom = (1.0 + R_dot / c_L) * delta + R / c_L * delta_dot - (1.5 - 0.5 * R_dot / c_L) * R_dot ** 2
    Den = (1.0 - R_dot / c_L) * R + 4.0 * mu_L / (c_L * par.rho_L)
    
    dxdt[1] = Nom / Den
    
    if pA1!=0.0 or pA2!=0.0:
        V_dot=4.0 * R * R * R_dot * np.pi;
        integrand_th = -(p * (1 + R_dot / c_L) + R / c_L * p_dot) * V_dot
        integrand_v = 16.0 * np.pi * mu_L * (R * R_dot*R_dot + R * R * R_dot * dxdt[1] / c_L)
        integrand_r = 4.0 * np.pi / c_L * R * R * R_dot * (R_dot * p + p_dot * R - 0.5 * par.rho_L * R_dot * R_dot * R_dot - par.rho_L * R * R_dot * dxdt[1])

        dxdt[-1]=(integrand_th + integrand_v + integrand_r)
    else:
        dxdt[-1]=0.0
    
    return dxdt


"""________________________________Solving________________________________"""

# This funfction solves the differential equation, and returns the numerical solution
# Error codes:
    # 0: succecfully solved with LSODA solver
    # 1: LSODA solver didn't converge, but Radau solver worked
    # 2: LSODA solver timed out, but Radau solver worked
    # 3: LSODA solver had a fatal error, but Radau solver worked
    # 4: LSODA solver failed, Radau solver didn't converge (NO SOLUTION!)
    # 5: LSODA solver failed, Radau solver timed out (NO SOLUTION!)
    # 6: LSODA solver failed, Radau solver had a fatal error (NO SOLUTION!) 
def solve(cpar, t_int=np.array([0.0, 1.0]), LSODA_timeout=30, Radau_timeout=300):
    error_code = 0
    start = time.time()
    if not 'P_v' in cpar:
        cpar.P_v = VapourPressure(T=cpar.T_inf) # [Pa]
    if not 'mu_L' in cpar:
        cpar.mu_L = Viscosity(T=cpar.T_inf) # [Pa]
    IC,negativepressure_error = InitialCondition(cpar)
    
    # solving d/dt x=f(t, x, cpar)
    try:
        num_sol = func_timeout(LSODA_timeout, solve_ivp, kwargs=dict(fun=f, t_span=t_int, y0=IC, method='LSODA', atol = 1e-10, rtol=1e-10, args=(cpar.P_amb,cpar.alfa_M,cpar.T_inf,cpar.surfactant,cpar.P_v,cpar.mu_L,cpar.freq1,cpar.freq2,cpar.pA1,cpar.pA2, cpar.theta_phase, cpar.c_L)))
        if num_sol.success == False:
            error_code = 1
    except FunctionTimedOut:
        error_code = 2
    except:
        error_code = 3
    if error_code != 0:
        try:
            num_sol = func_timeout(Radau_timeout, solve_ivp, kwargs=dict(fun=f, t_span=t_int, y0=IC, method='Radau', atol = 1e-10, rtol=1e-10, args=(cpar.P_amb,cpar.alfa_M,cpar.T_inf,cpar.surfactant,cpar.P_v,cpar.mu_L,cpar.freq1,cpar.freq2,cpar.pA1,cpar.pA2, cpar.theta_phase)))
            if num_sol.success == False:
                error_code = 4
        except FunctionTimedOut:
            error_code = 5
        except:
            error_code = 6
    
    end = time.time()
    elapsed_time = (end - start)
    
    if error_code > 3:
        return None, error_code, elapsed_time, negativepressure_error
    return num_sol, error_code, elapsed_time, negativepressure_error


"""________________________________Post processing________________________________"""

# This function gets the numerical solution and the control parameters, and returns some datas about the simulation
def get_data(cpar, num_sol, error_code, elapsed_time, negativepressure_error):
    # copy cpar:
    data = dotdict(dict(
        ID=cpar.ID,
        R_E=cpar.R_E,
        ratio=cpar.ratio,
        P_amb=cpar.P_amb,
        alfa_M=cpar.alfa_M,
        T_inf=cpar.T_inf,
        P_v=cpar.P_v,
        mu_L=cpar.mu_L,
        freq1=cpar.freq1,
        freq2=cpar.freq2,
        pA1=cpar.pA1,
        pA2=cpar.pA2,
        theta_phase=cpar.theta_phase,
        surfactant=cpar.surfactant,
        gases=cpar.gases,
        fractions=cpar.fractions
    ))
    
    # runtime and error
    data.c_L=cpar.c_L
    data.error_code = error_code
    data.elapsed_time = elapsed_time # [s]
    
    # default values
    if error_code > 3 or negativepressure_error:
        data.steps = 0
        loc_min = 0.0
        data.collapse_time = 0.0
        data.T_max = 0.0
        data.x_initial = np.zeros((4+par.K), dtype=np.float64)
        data.x_final = np.zeros((4+par.K), dtype=np.float64)
        data.n_H2 = 0.0
        data.n_O2 = 0.0
        data.n_NH3 = 0.0
        data.expansion_work = 0.0
        data.dissipated_acoustic_energy = 0.0
        data.energy_efficiency = 0.0
    
    # normal functioning
    else:
        data.steps = len(num_sol.t)
        data.x_initial = num_sol.y[:, 0] # initial values of [R, R_dot, T, c_1, ... c_K]
        
        # collapse time (first loc min of R)
        loc_min = argrelmin(num_sol.y[:][0])
        data.collapse_time = 0.0
        if not len(loc_min[0]) == 0:
            data.collapse_time = num_sol.t[loc_min[0][0]]
        
        # Energy calculations
        data.T_max = np.max(num_sol.y[:][2]) # maximum of temperature peaks [K]
        data.x_final = num_sol.y[:, -1] # final values of [R, R_dot, T, c_1, ... c_K]
        last_V = 4.0 / 3.0 * (100.0 * data.x_final[0]) ** 3 * np.pi # [cm^3]
        data.n_H2 = data.x_final[3+par.index['H2']] * last_V # [mol]
        data.n_O2 = data.x_final[3+par.index['O2']] * last_V # [mol]
        data.n_NH3 = data.x_final[3+par.index['NH3']] * last_V # [mol]
        m_H2 = 1.0e-3 * data.n_H2 * par.W[par.index['H2']] # [kg]
        m_NH3 = 1.0e-3 * data.n_NH3 * par.W[par.index['NH3']] # [kg]
        data.expansion_work = Work(cpar) # [J]
        data.dissipated_acoustic_energy = data.x_final[-1]  # [J]
        data.energy_efficiency = 1.0e-6 * (data.expansion_work+data.dissipated_acoustic_energy) / m_NH3 if cpar.pA1!=0.0 or cpar.pA2!=0.0 else 1.0e-6 * data.expansion_work / m_NH3 # [MJ/kg]
    return data

# keys of data: (except x_final)
keys = ['ID', 'R_E', 'ratio', 'P_amb', 'alfa_M', 'T_inf', 'P_v', 'mu_L', 'gases', 'fractions', 'surfactant', 'freq1', 'freq2', 'pA1', 'pA2', 'theta_phase', 'c_L', 'error_code', 'elapsed_time', 'steps', 'collapse_time', 'T_max', 'n_H2', 'n_O2', 'n_NH3', 'expansion_work', 'dissipated_acoustic_energy', 'energy_efficiency']

# This function prints the data dictionary in an organised way
def print_data(data, print_it=True):
    text = f'''Control parameters:
    ID ={data.ID: .0f}
    R_E ={1.0e6*data.R_E: .2f} [um]
    ratio ={data.ratio: .2f} [-]
    P_amb ={1.0e-5*data.P_amb: .2f} [bar]
    alfa_M ={data.alfa_M: .2f} [-]
    T_inf ={data.T_inf - 273.15: .2f} [°C]
    P_v ={data.P_v: .2f} [Pa]
    mu_L ={1000.0*data.mu_L: .2f} [mPa*s]
    surfactant ={data.surfactant: .2f} [-]    
    freq1 ={data.freq1: .0f} [Hz]
    freq2 ={data.freq2: .0f} [Hz]
    pA1 ={data.pA1: .0f} [Pa]
    pA2 ={data.pA2: .0f} [Pa]
    theta_phase={data.theta_phase: .2f} [rad]\n'''
    for gas, fraction in zip(data.gases, data.fractions):
        text += f'{int(100*fraction)}% {par.species[gas]}, ' 
    text = text[:-2] + f'''\nSimulation info:
    error_code ={data.error_code: .0f}
    elapsed_time ={data.elapsed_time: .2f} [s]
    steps ={data.steps: .0f} [-]'''
    
    text += f'''\nFinal state:
    R_final ={1e6*data.x_final[0]: .2f} [um];   R_dot_final ={data.x_final[1]} [m/s];   T_final ={data.x_final[2]: .2f} [K]
    n_H2 ={data.n_H2} [mol]; n_O2 ={data.n_O2} [mol]; n_NH3={data.n_NH3} [mol];
    Final molar concentrations: [mol/cm^3]\n        '''
    
    for k, specie in enumerate(par.species):
        text += f'{specie}: {data.x_final[3+k]};  '
        if (k+1) % 4 == 0: text += f'\n        '
    
    text += f'''\nResults:
    collapse_time = {data.collapse_time} [s]
    T_max ={data.T_max: .2f} [K]
    expansion work = {data.expansion_work} [J]
    dissipated acoustic energy = {data.dissipated_acoustic_energy} [J]
    ammonia production ={data.energy_efficiency: .2f} [MJ/kg]'''
    
    if print_it:
        print(text)
    else:
        return text
    
# This function runs solve() and get_data(), then return with data
# input and output is (or can be) normal dictionary
# it is used for multithreading (e.g. in bruteforce_parameter_study.inp)
def simulate(kwargs):
    args = dict(t_int=np.array([0.0, 1.0]), LSODA_timeout=30, Radau_timeout=300)
    for key in kwargs:
        args[key] = kwargs[key]
    args = dotdict(args)
    cpar = dotdict(args.cpar)
    num_sol, error_code, elapsed_time, negativepressure_error = solve(cpar, args.t_int, LSODA_timeout=args.LSODA_timeout, Radau_timeout=args.Radau_timeout)
    data = get_data(cpar, num_sol, error_code, elapsed_time, negativepressure_error)
    return dict(data)


"""________________________________Plotting________________________________"""

# This funfction solves the differential equation, and plots it
    # cpar: control parameters in a dictionary
    # t_int: time interval to solve the diffeq in (default: [0, 1] [s])
    #        graphs will be plotted in this intervall, if not default
    # n: how long should the plotted time interval be compared to the collapse time (default: 5 [-])
    # base_name: save plots as .png (default: '' alias do not save)
    #            use base_name='plot' --> plot_1.png, plot_2.png
    #            use base_name='images/plot' to save into images folder
    #            using a folder for images is recommend
    #            this folder have to be created manually
    # LSODA_timeout, Radau_timeout: timeout (maximum runtime) for different solvers in solve() in seconds
def plot(cpar, t_int=np.array([0.0, 1.0]), n=5.0, base_name='', LSODA_timeout=30, Radau_timeout=300):
    
    num_sol, error_code, elapsed_time, negativepressure_error = solve(cpar, t_int, LSODA_timeout, Radau_timeout)
    data = get_data(cpar, num_sol, error_code, elapsed_time, negativepressure_error)
    
# Error codes
    if error_code == 0:
        print(f'succecfully solved with LSODA solver')
    if error_code == 1:
        print(f'LSODA solver didn\'t converge, but Radau solver worked')
    if error_code == 2:
        print(f'LSODA solver timed out, but Radau solver worked')
    if error_code == 3:
        print(f'LSODA solver had a fatal error, but Radau solver worked')
        return None
    if error_code == 4:
        print(print(colored(f'LSODA solver failed, Radau solver didn\'t converge (NO SOLUTION!)','red')))
        return None
    if error_code == 5:
        print(print(colored(f'LSODA solver failed, Radau solver timed out (NO SOLUTION!)','red')))
        return None
    if error_code == 6:
        print(print(colored(f'LSODA solver failed, Radau solver had a fatal error (NO SOLUTION!)','red')))
        return None
    
# Calculations
    if t_int[1] != 1.0: 
        end_index = -1
    else:
        end_index = np.where(num_sol.t > n * data.collapse_time)[0][0]

    t = num_sol.t[:end_index] # [s]
    R = num_sol.y[0, :end_index] # [m]
    R_dot = num_sol.y[1, :end_index] # [m/s]
    T = num_sol.y[2, :end_index] # [K]
    c = num_sol.y[3:, :end_index] # [mol/cm^3]

    V = 4.0 / 3.0 * (100.0 * R) ** 3 * np.pi # [cm^3]
    n = c * V

# plot R and T
    plt.rcParams.update({'font.size': 18})
    fig1 = plt.figure(figsize=(20, 6))
    ax1 = fig1.add_subplot(axisbelow=True)
    ax2 = ax1.twinx()
    ax1.plot(t, R / cpar.R_E, color = 'b', linewidth = 1.0)
    ax2.plot(t, T, color = 'r', linewidth = 1.0, linestyle = '-.')

    ax1.set_ylabel('$y1$ [-]')
    ax1.set_xlabel('$t$ [s]')
    ax1.set_ylabel('$R/R_E$ [-]', color = 'b')
    ax2.set_ylabel('$T$ [K]', color = 'r')
    ax1.grid()
    
# textbox with initial conditions
    text = f"""Initial conditions:
    {'$R_E$':<25} {1e6*cpar.R_E: .2f}  $[\mu m]$
    {'$R_0/R_E$':<25} {cpar.ratio: .2f}  $[-]$
    {'$P_amb$':<25} {1e-5*cpar.P_amb: .2f}  $[bar]$
    {'$α_M$':<25} {cpar.alfa_M: .2f}  $[-]$
    {'$T_inf$':<25} {cpar.T_inf-273.15: .2f}  $[°C]$
    {'$P_{vapour}$':<25} {cpar.P_v: .1f}  $[Pa]$
    {'$μ_L$':<25} {1000*cpar.mu_L: .2f} $[mPa*s]$
    {'$surfactant$':<25} {cpar.surfactant: .2f}  $[-]$
    {'Initial content:':<20}
    """
    for gas, fraction in zip(cpar.gases, cpar.fractions):
        text += f'{int(100*fraction)}% {par.species[gas]}, ' 
    text = text[:-2]
    ax1.text(
        0.75, 0.95, # coordinates
        text, transform=ax1.transAxes,
        horizontalalignment='left', verticalalignment='top',
        fontsize=16, fontstyle='oblique',
        bbox={'facecolor': 'white', 'alpha': 1.0, 'pad': 10},
    )
    
    plt.show()

# plot reactions
    plt.rcParams.update({'font.size': 18})
    fig2 = plt.figure(figsize=(20, 9))
    ax = fig2.add_subplot(axisbelow=True)

    plt.ylim([1e-23, 1e-11])
    ax.set_yscale('log')
    #O,    H,    H2,     OH,   O2,      H2O,   HO2, H2O2,   O3,  OH_ex
    for i, specie in enumerate(par.species):
        ax.plot(t, n[i], label = '$' + specie + '$', linewidth = 1.0)

    ax.set_xlabel('$t$ [s]')
    ax.set_ylabel('$n_k$ [mol]')
    ax.grid()
    ax.legend()

    plt.show()
    
# saving the plots
    if base_name != '':
        try:
            fig1.savefig(base_name + '_1.png')
            fig2.savefig(base_name + '_2.png')
        except:
            print(print(colored(f'Error in saving {base_name}_1.png','red')))

# print data
    print_data(data)
    return None
    
#checks if a string is a number (float or int)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
        

"""________________________________Save to CSV________________________________"""

class Make_dir:
    # constructor
    def __init__(self, folder_name, file_base_name='output_', separator=','):
        self.folder_name = folder_name
        self.file_base_name = file_base_name
        self.separator = separator
        self.parent_dir = os.getcwd()
        self.save_dir = os.path.join(self.parent_dir, folder_name)
        self.number = 1    # uniqe ID number for csv files
        self.lines = 0    # number of data lines in currently opened CCSV
        self.is_opened = False    # True, if a CSV is opened
        
        if os.path.exists(self.save_dir):
            self.new = False
            self.number = len([1 for file in os.listdir(self.save_dir) if file[-4:] == '.csv']) + 1
            print(f'Folder already exists with {self.number-1} csv in it')
        else:
            self.new = True
            os.mkdir(self.save_dir)
    
    # makes a string from a list e.g. [1, 2, 3] -> '1,2,3'
    def list_to_string(self, array):
        line = ''
        for element in array:
            element = str(element).replace(',', ' ').replace('[', '').replace(']', '')
            if is_number(element):
                line += f'{float64(element):e}' + self.separator
            else:     
                line += element + self.separator
        return line[:-1]
        
    # writes a data dict into the currently opened file
    def write_line(self, data):
        line = self.list_to_string([data[key] for key in keys])
        line += self.separator + self.list_to_string([x for x in data['x_initial'][:-1]] + [x for x in data['x_final'][:-1]] + [data['expansion_work'],data['dissipated_acoustic_energy'],data['energy_efficiency']])
        self.file.write(line + '\n')
        self.lines += 1
        
    # saves a numerical solution
    def write_solution(self, data, num_sol, file_base_name):
    # create file containing data
        file = os.path.join(self.save_dir, file_base_name + '_data.csv')
        file = open(file, 'w')
        # write header line
        line = self.list_to_string(keys + ['R_0', 'R_dot_0', 'T_0'] + ['c_' + specie + '_0' for specie in par.species] + ['R_last', 'R_dot_last', 'T_last'] + ['c_' + specie + '_last' for specie in par.species] + ['expansion work','dissipated_acoustic_energy','energy_efficiency (NH3)'])
        file.write(line + '\n')
        # write data
        line = self.list_to_string([data[key]] for key in keys)
        line += self.separator + self.list_to_string([x for x in data.x_initial[:-1]] + [x for x in data.x_final[:-1]] + [data.expansion_work,data.dissipated_acoustic_energy,data.energy_efficiency])
        file.write(line + '\n')
        file.close()

    # create file containing num_sol
        file = os.path.join(self.save_dir, file_base_name + '_num_sol.csv')
        file = open(file, 'w')
        # write header line
        line = self.list_to_string(['t', 'R_0', 'R_dot_0', 'T_0'] + ['c_' + specie + '_0' for specie in par.species] + ['R', 'R_dot', 'T'] + ['c_' + specie for specie in par.species] + ['expansion work','dissipated_acoustic_energy','energy_efficiency (NH3)'])
        file.write(line + '\n')
        # write data
        for i in range(len(num_sol.t)):
            line = self.list_to_string([num_sol.t[i]] + list(num_sol.y[:-1, 0]) + list(num_sol.y[:-1, i]) + [data.expansion_work,num_sol.y[-1, i],1.0e-6 * (data.expansion_work+num_sol.y[-1,i]) / (1.0e-3 * num_sol.y[3+par.index['NH3'],i] * 4.0/3.0*np.pi*(100.0 *num_sol.y[0,i])**3 * par.W[par.index['NH3']])]) # [MJ/kg]  
            file.write(line + '\n')
        file.close()
    
    # create new file
    def new_file(self):
        if self.is_opened:
            return None
        file = os.path.join(self.save_dir, self.file_base_name + str(self.number) + '.csv')
        self.file = open(file, 'w')
        self.is_opened = True
        self.number += 1
        self.lines = 0
        # write header line:
        line = self.list_to_string(keys + ['R_0', 'R_dot_0', 'T_0'] + ['c_' + specie + '_0' for specie in par.species] + ['R_last', 'R_dot_last', 'T_last'] + ['c_' + specie + '_last' for specie in par.species] + ['expansion work','dissipated_acoustic_energy','energy_efficiency (NH3)'])
        self.file.write(line + '\n')
    
    # close file
    def close(self):
        if self.is_opened:
            self.file.close()
            self.is_opened = False
        
    # destructor
    def __del__(self):
        if self.is_opened:
            self.file.close()