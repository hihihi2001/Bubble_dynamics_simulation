"""
This is an automatically generated file.
This python file contains all the numerical constants and coefficents required for the simulations.
Recommended usage:
   importing: import parameters as par
   usage: print('Universal gas constant =', par.R_g)
"""

model = 'chem_Otomo2018_without_O'
import numpy as np

"""________________________________Physical constants________________________________"""

c_L            = 1483.0                   # Liquid sound speed at 30 °C [m/s]
rho_L          = 998.2                    # Liquid density [kg/m^3]
sigma          = 0.07197                  # Surface tension [N/m]
mu_L           = 0.001                    # Dynamic viscosity at 30 °C and 1 atm [Pa*s]
P_v            = 2338.1                   # Saturated vapour pressure at 30 °C [Pa]
alfa_M         = 0.35                     # water accommodation coefficient [-]
R_g            = 8.31446                  # Universal gas constant [J/mol/K]
R_erg          = 83144600.0               # Universal gas constant [erg/mol/K]
R_cal          = 1.987204                 # Universal gas constant [cal/mol/K]
N_A            = 6.02214e+23              # Avogadro's number [-]
h              = 6.62607015e-34           # Planck constant [m^2*kg/s]
R_v            = 461.521126               # Specific gas constant of water [J/kg/K]
erg2J          = 1e-07                    # Conversion factor from erg to J
cal2J          = 4.184                    # Conversion factor from cal to J
atm2Pa         = 101325.0                 # Conversion factor from atm to Pa
bar2Pa         = 100000.0                 # Conversion factor from bar to Pa
absolute_zero  = 273.15                   # Zero °C in Kelvin


"""________________________________Species________________________________"""

elements = np.array(['O','H','N','HE','AR'])
#                            0,         1,         2,         3,         4,         5,         6,         7,         8,         9,        10,        11
species = np.array([     'NH3',      'H2',       'H',     'NH2',      'NH',       'N',     'NNH',    'N2H4',    'N2H3',    'N2H2',    'H2NN',      'N2'])

# molar mass [g/mol]
W = np.array([        17.03061,   2.01594,   1.00797,  16.02264,  15.01467,   14.0067,  29.02137,  32.04528,  31.03731,  30.02934,  30.02934,   28.0134], dtype=np.float64)

# thermal conductivity [W / m / K]
lambdas = np.array([   0.00244,    0.1805,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,   0.02583], dtype=np.float64)

index = dict(
       NH3= 0,     H2= 1,      H= 2,    NH2= 3,     NH= 4,      N= 5,    NNH= 6,   N2H4= 7,   N2H3= 8,   N2H2= 9,
      H2NN=10,     N2=11
)

indexOfWater = -1
K = 12   # Number of species


"""________________________________NASA polynomials________________________________"""

N = 5    # degree of polynomials
TempRange = np.array([
    #   T_low   T_high    T_mid 
    [   200.0,  6000.0,  1000.0],    # NH3
    [   200.0,  6000.0,  1000.0],    # H2
    [   200.0,  6000.0,  1000.0],    # H
    [   200.0,  3000.0,  1000.0],    # NH2
    [   200.0,  6000.0,  1000.0],    # NH
    [   200.0,  6000.0,  1000.0],    # N
    [   200.0,  6000.0,  1000.0],    # NNH
    [   300.0,  5000.0,  1000.0],    # N2H4
    [   300.0,  5000.0,  1000.0],    # N2H3
    [   300.0,  5000.0,  1000.0],    # N2H2
    [   300.0,  5000.0,  1695.0],    # H2NN
    [   200.0,  6000.0,  1000.0]     # N2
], dtype=np.float64)

# LOW NASA coefficients
a_low = np.array([
    #             a_1              a_2              a_3              a_4              a_5              a_6              a_7 
    [      4.46075151,  -0.00568781763,  2.11411484e-05,  -2.0284998e-08,  6.89500555e-12,     -6707.53514,     -1.34450793],    # NH3
    [      2.34433112,   0.00798052075,  -1.9478151e-05,  2.01572094e-08, -7.37611761e-12,     -917.935173,     0.683010238],    # H2
    [             2.5,             0.0,             0.0,             0.0,             0.0,        25473.66,     -0.44668285],    # H
    [      4.19198016,  -0.00204602827,  6.67756134e-06, -5.24907235e-09,  1.55589948e-12,      21499.1387,   -0.0904785244],    # NH2
    [      3.49295037,   0.00031179572, -1.48906628e-06,  2.48167402e-09, -1.03570916e-12,      42105.9722,      1.84834973],    # NH
    [             2.5,             0.0,             0.0,             0.0,             0.0,       56104.638,       4.1939088],    # N
    [      4.25474632,  -0.00345098298,  1.37788699e-05, -1.33263744e-08,  4.41023397e-12,      28832.3793,      3.28551762],    # NNH
    [      0.06442606,       0.0274973,   -2.899451e-05,     1.74524e-08,   -4.422282e-12,        10451.92,        21.27789],    # N2H4
    [        3.174204,     0.004715907,    1.334867e-05,   -1.919685e-08,    7.487564e-12,         17272.7,        7.557224],    # N2H3
    [        1.617999,      0.01306312,   -1.715712e-05,    1.605608e-08,   -6.093639e-12,        24675.26,        13.79467],    # N2H2
    [      2.88544262,   0.00469495999,   7.0198323e-07, -1.53359038e-09,  3.79345858e-13,       33603.069,      8.95096779],    # H2NN
    [      3.53100528, -0.000123660988, -5.02999433e-07,  2.43530612e-09, -1.40881235e-12,     -1046.97628,      2.96747038]     # N2
], dtype=np.float64)

# LOW NASA coefficients
a_high = np.array([
    #             a_1              a_2              a_3              a_4              a_5              a_6              a_7 
    [      2.09566674,   0.00614750045, -2.00328925e-06,  3.01334626e-10, -1.71227204e-14,     -6309.45436,      9.59574081],    # NH3
    [      2.93286575,  0.000826608026, -1.46402364e-07,  1.54100414e-11,   -6.888048e-16,     -813.065581,     -1.02432865],    # H2
    [             2.5,             0.0,             0.0,             0.0,             0.0,        25473.66,     -0.44668285],    # H
    [      2.59263049,   0.00347683597, -1.08271624e-06,  1.49342558e-10, -5.75241187e-15,      21886.5421,      7.90565351],    # NH2
    [      2.78372644,   0.00132985888, -4.24785573e-07,  7.83494442e-11,  -5.5045131e-15,      42346.1945,      5.74084863],    # NH
    [       2.4159429,   0.00017489065,  -1.1902369e-07,   3.0226244e-11,  -2.0360983e-15,       56133.775,       4.6496095],    # N
    [      3.42744423,   0.00323295234, -1.17296299e-06,  1.90508356e-10, -1.14491506e-14,       28806.774,      6.39209233],    # NNH
    [        4.977317,     0.009595519,   -3.547639e-06,    6.124299e-10,   -4.029795e-14,        9341.219,        -2.96299],    # N2H4
    [        4.441846,     0.007214271,   -2.495684e-06,    3.920565e-10,    -2.29895e-14,        16642.21,      -0.4275205],    # N2H3
    [        3.371185,     0.006039968,   -2.303854e-06,    4.062789e-10,   -2.713144e-14,        24181.72,        4.980585],    # N2H2
    [      3.13531032,   0.00568632569, -1.93983467e-06,  3.01290501e-10, -1.74978144e-14,      33367.8346,       7.0481584],    # H2NN
    [      2.95257637,    0.0013969004, -4.92631603e-07,  7.86010195e-11, -4.60755204e-15,     -923.948688,      5.87188762]     # N2
], dtype=np.float64)


"""________________________________Reaction constants________________________________"""

I = 35    # Number of reactions
# Pre-exponential factors [cm^3/mol/s v 1/s]
A = np.array([
                 4.6e+19,             2.2e+16,            640000.0,           1000000.0,                 5.6,
                  9600.0,    70000000000000.0,   100000000000000.0,                0.57,    30000000000000.0,
            1000000000.0,   100000000000000.0,    50000000000000.0,    50000000000000.0,         170000000.0,
                 72000.0,  1500000000000000.0,   560000000000000.0,     7000000000000.0,     3900000000000.0,
                 3.6e+47,         240000000.0,            920000.0,    30000000000000.0,    20000000000000.0,
                 1.8e+40,             85000.0,               0.088,           2400000.0,             3.4e+26,
                 3.4e+26,         480000000.0,    70000000000000.0,           1800000.0,            1.89e+18
], dtype=np.float64)

# Temperature exponent [-]
b = np.array([
                    -1.4,                 0.0,                2.39,                2.32,                3.53,
                    2.46,                 0.0,                 0.0,                3.88,                 0.0,
                     0.0,                 0.0,                 0.0,                 0.0,                1.02,
                    1.88,                -0.5,              -0.414,                 0.0,                 0.0,
                  -10.38,                 1.5,                1.94,                 0.0,                 0.0,
                   -8.41,                2.63,                4.05,                 2.0,               -4.83,
                   -4.83,                 1.5,                 0.0,                1.94,               -0.85
], dtype=np.float64)

# Activation energy [cal/mol]
E = np.array([
                104380.0,             93470.0,             10171.0,               799.0,               552.0,
                   107.0,                 0.0,                 0.0,               342.0,                 0.0,
                     0.0,                 0.0,                 0.0,                 0.0,             11783.0,
                  8802.0,                 0.0,                66.0,              2500.0,              1500.0,
                 69009.0,               -10.0,             -1152.0,                 0.0,                 0.0,
                 73320.0,               230.0,              1610.0,             -1192.0,             46228.0,
                 46228.0,              -894.0,                 0.0,             -1152.0,            224950.0
], dtype=np.float64)


"""________________________________Reaction matrixes________________________________"""

# Forward reaction matrix
nu_forward = np.array([
    # NH3   H2    H  NH2   NH    N  NNH N2H4 N2H3 N2H2 H2NN   N2 
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  0. H2+M=H+H+M
    [   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  1. NH3+M=NH2+H+M
    [   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  2. NH3+H=NH2+H2
    [   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  3. NH2+H=NH+H2
    [   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0],    #  4. NH2+NH2=NH3+NH
    [   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0],    #  5. NH2+NH=NH3+N
    [   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0],    #  6. NH2+N=N2+H+H
    [   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  7. NH+H=N+H2
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0],    #  8. NH+NH=NH2+N
    [   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0],    #  9. NH+N=N2+H
    [   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 10. NNH=N2+H
    [   0,   0,   1,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 11. NNH+H=N2+H2
    [   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0],    # 12. NNH+NH=N2+NH2
    [   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0],    # 13. NNH+NH2=N2+NH3
    [   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0],    # 14. NH2+NH2=N2H2+H2
    [   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0],    # 15. NH2+NH2=H2NN+H2
    [   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0],    # 16. NH2+NH=N2H2+H
    [   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0],    # 17. NH2+NH2(+M)=N2H4(+M)
    [   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 18. N2H4+H=N2H3+H2
    [   0,   0,   0,   1,   0,   0,   0,   1,   0,   0,   0,   0],    # 19. N2H4+NH2=N2H3+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 20. N2H3=N2H2+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 21. N2H3+H=N2H2+H2
    [   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0],    # 22. N2H3+NH2=N2H2+NH3
    [   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0],    # 23. N2H3+NH2=H2NN+NH3
    [   0,   0,   0,   0,   1,   0,   0,   0,   1,   0,   0,   0],    # 24. N2H3+NH=N2H2+NH2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 25. N2H2=NNH+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 26. N2H2+H=NNH+H2
    [   0,   0,   0,   1,   0,   0,   0,   0,   0,   1,   0,   0],    # 27. N2H2+NH2=NNH+NH3
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0],    # 28. N2H2+NH=NNH+NH2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0],    # 29. H2NN=NNH+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0],    # 30. H2NN=NNH+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0],    # 31. H2NN+H=NNH+H2
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0],    # 32. H2NN+H=N2H2+H
    [   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   1,   0],    # 33. H2NN+NH2=NNH+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1]     # 34. N2+M=N+N+M
], dtype=np.float64)

# Backward reaction matrix
nu_backward = np.array([
    # NH3   H2    H  NH2   NH    N  NNH N2H4 N2H3 N2H2 H2NN   N2 
    [   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  0. H2+M=H+H+M
    [   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  1. NH3+M=NH2+H+M
    [   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  2. NH3+H=NH2+H2
    [   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  3. NH2+H=NH+H2
    [   1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  4. NH2+NH2=NH3+NH
    [   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    #  5. NH2+NH=NH3+N
    [   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   1],    #  6. NH2+N=N2+H+H
    [   0,   1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    #  7. NH+H=N+H2
    [   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0],    #  8. NH+NH=NH2+N
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1],    #  9. NH+N=N2+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 10. NNH=N2+H
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 11. NNH+H=N2+H2
    [   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1],    # 12. NNH+NH=N2+NH2
    [   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 13. NNH+NH2=N2+NH3
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 14. NH2+NH2=N2H2+H2
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0],    # 15. NH2+NH2=H2NN+H2
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 16. NH2+NH=N2H2+H
    [   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 17. NH2+NH2(+M)=N2H4(+M)
    [   0,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 18. N2H4+H=N2H3+H2
    [   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 19. N2H4+NH2=N2H3+NH3
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 20. N2H3=N2H2+H
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 21. N2H3+H=N2H2+H2
    [   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 22. N2H3+NH2=N2H2+NH3
    [   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0],    # 23. N2H3+NH2=H2NN+NH3
    [   0,   0,   0,   1,   0,   0,   0,   0,   0,   1,   0,   0],    # 24. N2H3+NH=N2H2+NH2
    [   0,   0,   1,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 25. N2H2=NNH+H
    [   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 26. N2H2+H=NNH+H2
    [   1,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 27. N2H2+NH2=NNH+NH3
    [   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0],    # 28. N2H2+NH=NNH+NH2
    [   0,   0,   1,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 29. H2NN=NNH+H
    [   0,   0,   1,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 30. H2NN=NNH+H
    [   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 31. H2NN+H=NNH+H2
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0],    # 32. H2NN+H=N2H2+H
    [   1,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 33. H2NN+NH2=NNH+NH3
    [   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0]     # 34. N2+M=N+N+M
], dtype=np.float64)

nu = nu_backward - nu_forward


"""________________________________Three-body reactions________________________________"""

ThirdBodyIndexes = np.array([   0,   1,  17,  34], dtype=np.int64)
ThirdBodyCount = 4

# third-body efficiency factors
alfa = np.array([
    #     NH3       H2        H      NH2       NH        N      NNH     N2H4     N2H3     N2H2     H2NN       N2 
    [     1.0,     2.5,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0],    #  0. H2+M=H+H+M
    [     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0],    #  1. NH3+M=NH2+H+M
    [     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0],    # 17. NH2+NH2(+M)=N2H4(+M)
    [     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0]     # 34. N2+M=N+N+M
], dtype=np.float64)


"""________________________________Irreversible reactions________________________________"""

IrreversibleIndexes = np.array([], dtype=np.int64)
IrreversibleCount = 0


"""________________________________Pressure-dependent reactions________________________________"""

PressureDependentIndexes = np.array([  17], dtype=np.int64)
PressureDependentCount = 1

LindemannIndexes = np.array([], dtype=np.int64)
LindemannCount = 0

# Fall-off parameters
ReacConst = np.array([
    #               A_0                b_0                E_0 
    [           1.6e+34,             -5.49,            1987.0]     # 17. NH2+NH2(+M)=N2H4(+M)
], dtype=np.float64)

TroeIndexes = np.array([  17], dtype=np.int64)
TroeCount = 1

# Troe parameters
Troe = np.array([
    #              alfa               T***                 T*                T** 
    [              0.31,             1e-30,             1e+30,             1e+30]     # 17. NH2+NH2(+M)=N2H4(+M)
], dtype=np.float64)

SRIIndexes = np.array([], dtype=np.int64)
SRICount = 0

# SRI parameters
SRI = np.array([
    #                 a                  b                  c                  d                  e 
    [] 
], dtype=np.float64)

PlogIndexes = np.array([  20,  25,  29,  30], dtype=np.int64)
PlogStart = np.array([   0,   3,   6,   9], dtype=np.int64)
PlogStop = np.array([   3,   6,   9,  12], dtype=np.int64)
PlogCount = 4

# PLOG parameters
Plog = np.array([
    #               P_1                A_1                b_1                E_1 
    [           10000.0,           2.3e+43,             -9.55,           64468.0],    # 20. N2H3=N2H2+H
    [          100000.0,           3.6e+47,            -10.38,           69009.0],    # 
    [         1000000.0,           1.8e+45,             -9.39,           70141.0],    # 
    [           10000.0,           5.6e+36,             -7.75,           70340.0],    # 25. N2H2=NNH+H
    [          100000.0,           1.8e+40,             -8.41,           73320.0],    # 
    [         1000000.0,           3.1e+41,             -8.42,           76102.0],    # 
    [           10000.0,           5.9e+32,             -6.99,           51791.0],    # 29. H2NN=NNH+H
    [          100000.0,           9.6e+35,             -7.57,           54841.0],    # 
    [         1000000.0,             5e+36,             -7.43,           57295.0],    # 
    [           10000.0,           7.2e+28,             -7.77,           50758.0],    # 30. H2NN=NNH+H
    [          100000.0,           3.2e+31,             -6.22,           52318.0],    # 
    [         1000000.0,           5.1e+33,             -6.52,           54215.0]     # 
], dtype=np.float64)

