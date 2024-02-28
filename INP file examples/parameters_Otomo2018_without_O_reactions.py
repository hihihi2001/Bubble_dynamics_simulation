"""
This is an automatically generated file.
This python file contains all the numerical constants and coefficents required for the simulations.
Recommended usage:
   importing: import parameters as par
   usage: print('Universal gas constant =', par.R_g)
"""

model = 'chem_Otomo2018_without_O_reactions'
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
species = np.array([
          'NO',     'NH3',      'H2',      'O2',       'H',       'O',      'OH',     'HO2',     'H2O',    'H2O2',
         'NH2',      'NH',       'N',     'NNH',   'NH2OH',    'H2NO',    'HNOH',     'HNO',     'HON',     'NO2',
        'HONO',    'HNO2',     'NO3',   'HONO2',     'N2O',    'N2H4',    'N2H3',    'N2H2',    'H2NN',      'AR',
          'HE',      'N2'
])

# molar mass [g/mol]
W = np.array([      
       30.0061,  17.03061,   2.01594,   31.9988,   1.00797,   15.9994,  17.00737,  33.00677,  18.01534,  34.01474,
      16.02264,  15.01467,   14.0067,  29.02137,  33.03001,  32.02204,  32.02204,  31.01407,  31.01407,   46.0055,
      47.01347,  47.01347,   62.0049,  63.01287,   44.0128,  32.04528,  31.03731,  30.02934,  30.02934,    39.948,
        4.0026,   28.0134
], dtype=np.float64)

# thermal conductivity [W / m / K]
lambdas = np.array([
           0.0,   0.00244,    0.1805,   0.02658,       0.0,       0.0,       0.0,       0.0,     0.016,    0.5863,
           0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,   0.00988,
           0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,       0.0,    0.0177,
         0.151,   0.02583
], dtype=np.float64)

index = dict(
        NO= 0,    NH3= 1,     H2= 2,     O2= 3,      H= 4,      O= 5,     OH= 6,    HO2= 7,    H2O= 8,   H2O2= 9,
       NH2=10,     NH=11,      N=12,    NNH=13,  NH2OH=14,   H2NO=15,   HNOH=16,    HNO=17,    HON=18,    NO2=19,
      HONO=20,   HNO2=21,    NO3=22,  HONO2=23,    N2O=24,   N2H4=25,   N2H3=26,   N2H2=27,   H2NN=28,     AR=29,
        HE=30,     N2=31
)

indexOfWater = 8
K = 32   # Number of species


"""________________________________NASA polynomials________________________________"""

N = 5    # degree of polynomials
TempRange = np.array([
    #   T_low   T_high    T_mid 
    [   200.0,  6000.0,  1000.0],    # NO
    [   200.0,  6000.0,  1000.0],    # NH3
    [   200.0,  6000.0,  1000.0],    # H2
    [   200.0,  6000.0,  1000.0],    # O2
    [   200.0,  6000.0,  1000.0],    # H
    [   200.0,  6000.0,  1000.0],    # O
    [   200.0,  6000.0,  1000.0],    # OH
    [   200.0,  5000.0,  1000.0],    # HO2
    [   200.0,  6000.0,  1000.0],    # H2O
    [   200.0,  6000.0,  1000.0],    # H2O2
    [   200.0,  3000.0,  1000.0],    # NH2
    [   200.0,  6000.0,  1000.0],    # NH
    [   200.0,  6000.0,  1000.0],    # N
    [   200.0,  6000.0,  1000.0],    # NNH
    [   200.0,  6000.0,  1000.0],    # NH2OH
    [   298.0,  3000.0,  1000.0],    # H2NO
    [   200.0,  6000.0,  1000.0],    # HNOH
    [   200.0,  6000.0,  1000.0],    # HNO
    [   200.0,  6000.0,  1000.0],    # HON
    [   200.0,  6000.0,  1000.0],    # NO2
    [   200.0,  6000.0,  1000.0],    # HONO
    [   300.0,  4000.0,  1500.0],    # HNO2
    [   200.0,  6000.0,  1000.0],    # NO3
    [   200.0,  6000.0,  1000.0],    # HONO2
    [   200.0,  6000.0,  1000.0],    # N2O
    [   300.0,  5000.0,  1000.0],    # N2H4
    [   300.0,  5000.0,  1000.0],    # N2H3
    [   300.0,  5000.0,  1000.0],    # N2H2
    [   300.0,  5000.0,  1695.0],    # H2NN
    [   200.0,  6000.0,  1000.0],    # AR
    [   200.0,  6000.0,  1000.0],    # HE
    [   200.0,  6000.0,  1000.0]     # N2
], dtype=np.float64)

# LOW NASA coefficients
a_low = np.array([
    #             a_1              a_2              a_3              a_4              a_5              a_6              a_7 
    [      4.21859896,  -0.00463988124,  1.10443049e-05, -9.34055507e-09,  2.80554874e-12,      9845.09964,      2.28061001],    # NO
    [      4.46075151,  -0.00568781763,  2.11411484e-05,  -2.0284998e-08,  6.89500555e-12,     -6707.53514,     -1.34450793],    # NH3
    [      2.34433112,   0.00798052075,  -1.9478151e-05,  2.01572094e-08, -7.37611761e-12,     -917.935173,     0.683010238],    # H2
    [      3.78245636,  -0.00299673416,  9.84730201e-06, -9.68129509e-09,  3.24372837e-12,     -1063.94356,      3.65767573],    # O2
    [             2.5,             0.0,             0.0,             0.0,             0.0,        25473.66,     -0.44668285],    # H
    [       3.1682671,  -0.00327931884,  6.64306396e-06, -6.12806624e-09,  2.11265971e-12,      29122.2592,      2.05193346],    # O
    [      3.99198424,  -0.00240106655,  4.61664033e-06, -3.87916306e-09,  1.36319502e-12,      3368.89836,    -0.103998477],    # OH
    [      4.30179807,  -0.00474912097,  2.11582905e-05, -2.42763914e-08,  9.29225225e-12,      264.018485,       3.7166622],    # HO2
    [       4.1986352,   -0.0020364017,   6.5203416e-06,  -5.4879269e-09,    1.771968e-12,      -30293.726,     -0.84900901],    # H2O
    [      4.31515149, -0.000847390622,  1.76404323e-05, -2.26762944e-08,  9.08950158e-12,     -17706.7437,      3.27373319],    # H2O2
    [      4.19198016,  -0.00204602827,  6.67756134e-06, -5.24907235e-09,  1.55589948e-12,      21499.1387,   -0.0904785244],    # NH2
    [      3.49295037,   0.00031179572, -1.48906628e-06,  2.48167402e-09, -1.03570916e-12,      42105.9722,      1.84834973],    # NH
    [             2.5,             0.0,             0.0,             0.0,             0.0,       56104.638,       4.1939088],    # N
    [      4.25474632,  -0.00345098298,  1.37788699e-05, -1.33263744e-08,  4.41023397e-12,      28832.3793,      3.28551762],    # NNH
    [      3.21016092,   0.00619671676,  1.10594948e-05, -1.96668262e-08,   8.8251659e-12,     -6581.48481,      7.93293571],    # NH2OH
    [      4.07694692,   0.00021917994,  9.92160372e-06, -1.02259681e-08,  3.26220462e-12,      6485.47616,      3.93185152],    # H2NO
    [      3.95608248,   -0.0030261102,  2.56874396e-05,  -3.1564512e-08,  1.24084574e-11,       10919.979,      5.55950983],    # HNOH
    [      4.53525574,  -0.00568543377,   1.8519854e-05, -1.71881225e-08,  5.55818157e-12,      11618.3003,      1.74315886],    # HNO
    [      4.30796097,  -0.00501538487,  2.27054537e-05, -2.65676371e-08,  1.02998699e-11,      24585.0141,      3.93009562],    # HON
    [       3.9440312,    -0.001585429,   1.6657812e-05,  -2.0475426e-08,   7.8350564e-12,        2896.618,       6.3119919],    # NO2
    [      3.21415915,   0.00812778066,  1.65998916e-06, -9.52814708e-09,  4.87131424e-12,     -10783.0727,      9.82200056],    # HONO
    [        1.934838,      0.01010036,   -4.964616e-06,     8.70112e-10,   -2.324135e-15,     -5915.71591,      14.7282082],    # HNO2
    [       2.1735933,    0.0104902685,  1.10472669e-05, -2.81561867e-08,   1.3658396e-11,      7812.90905,       14.602209],    # NO3
    [      1.69329154,    0.0190167702, -8.25176697e-06, -6.06113827e-09,  4.65236978e-12,     -17388.2411,      17.1839655],    # HONO2
    [       2.2571502,     0.011304728,  -1.3671319e-05,   9.6819803e-09,  -2.9307182e-12,       8741.7746,       10.757992],    # N2O
    [      0.06442606,       0.0274973,   -2.899451e-05,     1.74524e-08,   -4.422282e-12,        10451.92,        21.27789],    # N2H4
    [        3.174204,     0.004715907,    1.334867e-05,   -1.919685e-08,    7.487564e-12,         17272.7,        7.557224],    # N2H3
    [        1.617999,      0.01306312,   -1.715712e-05,    1.605608e-08,   -6.093639e-12,        24675.26,        13.79467],    # N2H2
    [      2.88544262,   0.00469495999,   7.0198323e-07, -1.53359038e-09,  3.79345858e-13,       33603.069,      8.95096779],    # H2NN
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,      4.37967491],    # AR
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,     0.928723974],    # HE
    [      3.53100528, -0.000123660988, -5.02999433e-07,  2.43530612e-09, -1.40881235e-12,     -1046.97628,      2.96747038]     # N2
], dtype=np.float64)

# LOW NASA coefficients
a_high = np.array([
    #             a_1              a_2              a_3              a_4              a_5              a_6              a_7 
    [      3.26071234,   0.00119101135, -4.29122646e-07,  6.94481463e-11, -4.03295681e-15,      9921.43132,      6.36900518],    # NO
    [      2.09566674,   0.00614750045, -2.00328925e-06,  3.01334626e-10, -1.71227204e-14,     -6309.45436,      9.59574081],    # NH3
    [      2.93286575,  0.000826608026, -1.46402364e-07,  1.54100414e-11,   -6.888048e-16,     -813.065581,     -1.02432865],    # H2
    [      3.66096065,  0.000656365811, -1.41149627e-07,  2.05797935e-11, -1.29913436e-15,     -1215.97718,      3.41536279],    # O2
    [             2.5,             0.0,             0.0,             0.0,             0.0,        25473.66,     -0.44668285],    # H
    [      2.54363697, -2.73162486e-05,  -4.1902952e-09,  4.95481845e-12, -4.79553694e-16,       29226.012,      4.92229457],    # O
    [      2.83853033,   0.00110741289, -2.94000209e-07,  4.20698729e-11,  -2.4228989e-15,      3697.80808,      5.84494652],    # OH
    [      4.17228741,   0.00188117627, -3.46277286e-07,  1.94657549e-11,  1.76256905e-16,      31.0206839,      2.95767672],    # HO2
    [       2.6770389,    0.0029731816,  -7.7376889e-07,   9.4433514e-11,  -4.2689991e-15,      -29885.894,         6.88255],    # H2O
    [      4.57977305,   0.00405326003,  -1.2984473e-06,    1.982114e-10, -1.13968792e-14,     -18007.1775,     0.664970694],    # H2O2
    [      2.59263049,   0.00347683597, -1.08271624e-06,  1.49342558e-10, -5.75241187e-15,      21886.5421,      7.90565351],    # NH2
    [      2.78372644,   0.00132985888, -4.24785573e-07,  7.83494442e-11,  -5.5045131e-15,      42346.1945,      5.74084863],    # NH
    [       2.4159429,   0.00017489065,  -1.1902369e-07,   3.0226244e-11,  -2.0360983e-15,       56133.775,       4.6496095],    # N
    [      3.42744423,   0.00323295234, -1.17296299e-06,  1.90508356e-10, -1.14491506e-14,       28806.774,      6.39209233],    # NNH
    [      3.88112502,   0.00815708448, -2.82615576e-06,  4.37930933e-10, -2.52724604e-14,     -6860.18419,      3.79156136],    # NH2OH
    [      3.33719385,   0.00572250531, -2.14985397e-06,  3.65983461e-10, -2.18615301e-14,      6506.21112,      6.86465421],    # H2NO
    [      3.98321933,   0.00488846374, -1.65086637e-06,  2.55371446e-10, -1.48308561e-14,      10578.0106,      3.62582838],    # HNOH
    [      3.16598124,   0.00299958892, -3.94376786e-07, -3.85344089e-11,  7.07602668e-15,      11772.6311,      7.64511172],    # HNO
    [      4.00745749,   0.00241824666, -8.13734001e-07,  1.25573064e-10, -7.28062602e-15,      24396.5586,      4.01091333],    # HON
    [        4.884754,    0.0021723955,  -8.2806909e-07,    1.574751e-10,  -1.0510895e-14,       2316.4982,     -0.11741695],    # NO2
    [      5.79182717,   0.00365162554,  -1.2929339e-06,  2.06892796e-10, -1.23154749e-14,     -11595.3895,     -4.05538852],    # HONO
    [         6.47963,     0.001995274,   -1.740387e-07,   -9.695872e-11,     1.70148e-14,     -7809.50291,     -10.6771518],    # HNO2
    [      7.48347702,   0.00257772064, -1.00945831e-06,  1.72314063e-10, -1.07154008e-14,      6129.90474,     -14.1618136],    # NO3
    [      8.03098942,   0.00446958589, -1.72459491e-06,  2.91556153e-10, -1.80102702e-14,     -19282.1685,      -16.261672],    # HONO2
    [       4.8230729,    0.0026270251,  -9.5850872e-07,   1.6000712e-10,  -9.7752302e-15,       8073.4047,      -2.2017208],    # N2O
    [        4.977317,     0.009595519,   -3.547639e-06,    6.124299e-10,   -4.029795e-14,        9341.219,        -2.96299],    # N2H4
    [        4.441846,     0.007214271,   -2.495684e-06,    3.920565e-10,    -2.29895e-14,        16642.21,      -0.4275205],    # N2H3
    [        3.371185,     0.006039968,   -2.303854e-06,    4.062789e-10,   -2.713144e-14,        24181.72,        4.980585],    # N2H2
    [      3.13531032,   0.00568632569, -1.93983467e-06,  3.01290501e-10, -1.74978144e-14,      33367.8346,       7.0481584],    # H2NN
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,      4.37967491],    # AR
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,     0.928723974],    # HE
    [      2.95257637,    0.0013969004, -4.92631603e-07,  7.86010195e-11, -4.60755204e-15,     -923.948688,      5.87188762]     # N2
], dtype=np.float64)


"""________________________________Reaction constants________________________________"""

I = 36    # Number of reactions
# Pre-exponential factors [cm^3/mol/s v 1/s]
A = np.array([
                 4.6e+19,             5.8e+18,             2.2e+16,            640000.0,           1000000.0,
                     5.6,              9600.0,    70000000000000.0,   100000000000000.0,                0.57,
        30000000000000.0,        1000000000.0,   100000000000000.0,    50000000000000.0,    50000000000000.0,
             170000000.0,             72000.0,  1500000000000000.0,   560000000000000.0,     7000000000000.0,
         3900000000000.0,             3.6e+47,         240000000.0,            920000.0,    30000000000000.0,
        20000000000000.0,             1.8e+40,             85000.0,               0.088,           2400000.0,
                 3.4e+26,             3.4e+26,         480000000.0,    70000000000000.0,           1800000.0,
                1.89e+18
], dtype=np.float64)

# Temperature exponent [-]
b = np.array([
                    -1.4,                -1.1,                 0.0,                2.39,                2.32,
                    3.53,                2.46,                 0.0,                 0.0,                3.88,
                     0.0,                 0.0,                 0.0,                 0.0,                 0.0,
                    1.02,                1.88,                -0.5,              -0.414,                 0.0,
                     0.0,              -10.38,                 1.5,                1.94,                 0.0,
                     0.0,               -8.41,                2.63,                4.05,                 2.0,
                   -4.83,               -4.83,                 1.5,                 0.0,                1.94,
                   -0.85
], dtype=np.float64)

# Activation energy [cal/mol]
E = np.array([
                104380.0,            104380.0,             93470.0,             10171.0,               799.0,
                   552.0,               107.0,                 0.0,                 0.0,               342.0,
                     0.0,                 0.0,                 0.0,                 0.0,                 0.0,
                 11783.0,              8802.0,                 0.0,                66.0,              2500.0,
                  1500.0,             69009.0,               -10.0,             -1152.0,                 0.0,
                     0.0,             73320.0,               230.0,              1610.0,             -1192.0,
                 46228.0,             46228.0,              -894.0,                 0.0,             -1152.0,
                224950.0
], dtype=np.float64)


"""________________________________Reaction matrixes________________________________"""

# Forward reaction matrix
nu_forward = np.array([
    #  NO  NH3   H2   O2    H    O   OH  HO2  H2O H2O2  NH2   NH    N  NNH NH2OH H2NO HNOH  HNO  HON  NO2 HONO HNO2  NO3 HONO2  N2O N2H4 N2H3 N2H2 H2NN   AR   HE   N2 
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  0. H2+M=H+H+M
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0],    #  1. H2+AR=H+H+AR
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  2. NH3+M=NH2+H+M
    [   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  3. NH3+H=NH2+H2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  4. NH2+H=NH+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  5. NH2+NH2=NH3+NH
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  6. NH2+NH=NH3+N
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  7. NH2+N=N2+H+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  8. NH+H=N+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  9. NH+NH=NH2+N
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 10. NH+N=N2+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 11. NNH=N2+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 12. NNH+H=N2+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 13. NNH+NH=N2+NH2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 14. NNH+NH2=N2+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 15. NH2+NH2=N2H2+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 16. NH2+NH2=H2NN+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 17. NH2+NH=N2H2+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 18. NH2+NH2(+M)=N2H4(+M)
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    # 19. N2H4+H=N2H3+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    # 20. N2H4+NH2=N2H3+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 21. N2H3=N2H2+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 22. N2H3+H=N2H2+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 23. N2H3+NH2=N2H2+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 24. N2H3+NH2=H2NN+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 25. N2H3+NH=N2H2+NH2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 26. N2H2=NNH+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 27. N2H2+H=NNH+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 28. N2H2+NH2=NNH+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 29. N2H2+NH=NNH+NH2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 30. H2NN=NNH+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 31. H2NN=NNH+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 32. H2NN+H=NNH+H2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 33. H2NN+H=N2H2+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 34. H2NN+NH2=NNH+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1]     # 35. N2+M=N+N+M
], dtype=np.float64)

# Backward reaction matrix
nu_backward = np.array([
    #  NO  NH3   H2   O2    H    O   OH  HO2  H2O H2O2  NH2   NH    N  NNH NH2OH H2NO HNOH  HNO  HON  NO2 HONO HNO2  NO3 HONO2  N2O N2H4 N2H3 N2H2 H2NN   AR   HE   N2 
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  0. H2+M=H+H+M
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0],    #  1. H2+AR=H+H+AR
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  2. NH3+M=NH2+H+M
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  3. NH3+H=NH2+H2
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  4. NH2+H=NH+H2
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  5. NH2+NH2=NH3+NH
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  6. NH2+NH=NH3+N
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    #  7. NH2+N=N2+H+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  8. NH+H=N+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  9. NH+NH=NH2+N
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 10. NH+N=N2+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 11. NNH=N2+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 12. NNH+H=N2+H2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 13. NNH+NH=N2+NH2
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 14. NNH+NH2=N2+NH3
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 15. NH2+NH2=N2H2+H2
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 16. NH2+NH2=H2NN+H2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 17. NH2+NH=N2H2+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    # 18. NH2+NH2(+M)=N2H4(+M)
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 19. N2H4+H=N2H3+H2
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],    # 20. N2H4+NH2=N2H3+NH3
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 21. N2H3=N2H2+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 22. N2H3+H=N2H2+H2
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 23. N2H3+NH2=N2H2+NH3
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 24. N2H3+NH2=H2NN+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 25. N2H3+NH=N2H2+NH2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 26. N2H2=NNH+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 27. N2H2+H=NNH+H2
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 28. N2H2+NH2=NNH+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 29. N2H2+NH=NNH+NH2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 30. H2NN=NNH+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 31. H2NN=NNH+H
    [   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 32. H2NN+H=NNH+H2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 33. H2NN+H=N2H2+H
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 34. H2NN+NH2=NNH+NH3
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0]     # 35. N2+M=N+N+M
], dtype=np.float64)

nu = nu_backward - nu_forward


"""________________________________Three-body reactions________________________________"""

ThirdBodyIndexes = np.array([   0,   2,  18,  35], dtype=np.int64)
ThirdBodyCount = 4

# third-body efficiency factors
alfa = np.array([
    #      NO      NH3       H2       O2        H        O       OH      HO2      H2O     H2O2      NH2       NH        N      NNH    NH2OH     H2NO     HNOH      HNO      HON      NO2     HONO     HNO2      NO3    HONO2      N2O     N2H4     N2H3     N2H2     H2NN       AR       HE       N2 
    [     1.0,     1.0,     2.5,     1.0,     1.0,     1.0,     1.0,     1.0,    12.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     0.0,     1.0,     1.0],    #  0. H2+M=H+H+M
    [     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0],    #  2. NH3+M=NH2+H+M
    [     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0],    # 18. NH2+NH2(+M)=N2H4(+M)
    [     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0,     1.0]     # 35. N2+M=N+N+M
], dtype=np.float64)


"""________________________________Irreversible reactions________________________________"""

IrreversibleIndexes = np.array([], dtype=np.int64)
IrreversibleCount = 0


"""________________________________Pressure-dependent reactions________________________________"""

PressureDependentIndexes = np.array([  18], dtype=np.int64)
PressureDependentCount = 1

LindemannIndexes = np.array([], dtype=np.int64)
LindemannCount = 0

# Fall-off parameters
ReacConst = np.array([
    #               A_0                b_0                E_0 
    [           1.6e+34,             -5.49,            1987.0]     # 18. NH2+NH2(+M)=N2H4(+M)
], dtype=np.float64)

TroeIndexes = np.array([  18], dtype=np.int64)
TroeCount = 1

# Troe parameters
Troe = np.array([
    #              alfa               T***                 T*                T** 
    [              0.31,             1e-30,             1e+30,             1e+30]     # 18. NH2+NH2(+M)=N2H4(+M)
], dtype=np.float64)

SRIIndexes = np.array([], dtype=np.int64)
SRICount = 0

# SRI parameters
SRI = np.array([
    #                 a                  b                  c                  d                  e 
    [] 
], dtype=np.float64)

PlogIndexes = np.array([  21,  26,  30,  31], dtype=np.int64)
PlogStart = np.array([   0,   3,   6,   9], dtype=np.int64)
PlogStop = np.array([   3,   6,   9,  12], dtype=np.int64)
PlogCount = 4

# PLOG parameters
Plog = np.array([
    #               P_1                A_1                b_1                E_1 
    [           10000.0,           2.3e+43,             -9.55,           64468.0],    # 21. N2H3=N2H2+H
    [          100000.0,           3.6e+47,            -10.38,           69009.0],    # 
    [         1000000.0,           1.8e+45,             -9.39,           70141.0],    # 
    [           10000.0,           5.6e+36,             -7.75,           70340.0],    # 26. N2H2=NNH+H
    [          100000.0,           1.8e+40,             -8.41,           73320.0],    # 
    [         1000000.0,           3.1e+41,             -8.42,           76102.0],    # 
    [           10000.0,           5.9e+32,             -6.99,           51791.0],    # 30. H2NN=NNH+H
    [          100000.0,           9.6e+35,             -7.57,           54841.0],    # 
    [         1000000.0,             5e+36,             -7.43,           57295.0],    # 
    [           10000.0,           7.2e+28,             -7.77,           50758.0],    # 31. H2NN=NNH+H
    [          100000.0,           3.2e+31,             -6.22,           52318.0],    # 
    [         1000000.0,           5.1e+33,             -6.52,           54215.0]     # 
], dtype=np.float64)

