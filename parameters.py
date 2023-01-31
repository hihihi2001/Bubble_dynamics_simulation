"""
This is an automatically generated file.
This python file contains all the numerical constants and coefficents required for the simulations.
Recommended usage:
   importing: import parameters as par
   usage: print('Universal gas constant =', par.R_g)
"""

model = 'chemkin_AR_HE'
import numpy as np

"""________________________________Physical constants________________________________"""
c_L = 1483.0       # Liquid sound speed [m/s]
rho_L = 998.2      # Liquid density [kg/m^3]
sigma = 71.97e-3   # Surface tension [N/m]
mu_L = 0.001       # Dynamic viscosity [Pa*s]
R_v = 461.5227     # Specific gas constant of water [J/kg/K]

R_g = 8.31446      # Universal gas constant [J/mol/K]
R_erg = 8.31446e7  # Universal gas constant [erg/mol/K]
R_cal = 1.987      # Universal gas constant [cal/mol/K]
N_A = 6.02214e23   # Avogadro's number [-]
h = 6.62607015e-34 # Planck constant [m^2*kg/s]


"""________________________________Species________________________________"""
elements = np.array(['C','H','N','O','AR','HE'])
#                            0,         1,         2,         3,         4,         5,         6,         7,         8,         9,        10,        11
species = np.array([       'H',      'H2',       'O',      'O2',      'OH',     'H2O',      'N2',     'HO2',    'H2O2',      'AR',      'HE',    'OHEX'])
# molar mass [g/mol]
W = np.array([         1.00797,   2.01594,   15.9994,   31.9988,  17.00737,  18.01534,   28.0134,  33.00677,  34.01474,    39.948,    4.0026,  17.00737], dtype=np.float64)
# thermal conductivity [W / m / K]
lambdas = np.array([       0.0,    0.1805,       0.0,   0.02658,       0.0,     0.598,   0.02583,       0.0,    0.5863,   0.01772,    0.1513,       0.0], dtype=np.float64)
index = dict(
         H= 0,     H2= 1,      O= 2,     O2= 3,     OH= 4,    H2O= 5,     N2= 6,    HO2= 7,   H2O2= 8,     AR= 9,
        HE=10,   OHEX=11
)
indexOfWater = 5
K = 12   # Number of species


"""________________________________NASA polynomials________________________________"""
N = 5    # degree of polynomials
TempRange = np.array([
    #   T_low   T_high    T_mid 
    [   200.0,  6000.0,  1000.0],    # H
    [   200.0,  6000.0,  1000.0],    # H2
    [   200.0,  6000.0,  1000.0],    # O
    [   200.0,  6000.0,  1000.0],    # O2
    [   200.0,  6000.0,  1000.0],    # OH
    [   200.0,  6000.0,  1000.0],    # H2O
    [   200.0,  6000.0,  1000.0],    # N2
    [   200.0,  5000.0,  1000.0],    # HO2
    [   200.0,  6000.0,  1000.0],    # H2O2
    [   200.0,  6000.0,  1000.0],    # AR
    [   200.0,  6000.0,  1000.0],    # HE
    [   300.0,  5000.0,  1000.0]     # OHEX
], dtype=np.float64)

# LOW NASA coefficients
a_low = np.array([
    #             a_1              a_2              a_3              a_4              a_5              a_6              a_7 
    [             2.5,             0.0,             0.0,             0.0,             0.0,        25473.66,     -0.44668285],    # H
    [      2.34433112,   0.00798052075,  -1.9478151e-05,  2.01572094e-08, -7.37611761e-12,     -917.935173,     0.683010238],    # H2
    [       3.1682671,  -0.00327931884,  6.64306396e-06, -6.12806624e-09,  2.11265971e-12,      29122.2592,      2.05193346],    # O
    [      3.78245636,  -0.00299673416,  9.84730201e-06, -9.68129509e-09,  3.24372837e-12,     -1063.94356,      3.65767573],    # O2
    [      3.99198424,  -0.00240106655,  4.61664033e-06, -3.87916306e-09,  1.36319502e-12,      3368.89836,    -0.103998477],    # OH
    [       4.1986352,   -0.0020364017,   6.5203416e-06,  -5.4879269e-09,    1.771968e-12,      -30293.726,     -0.84900901],    # H2O
    [      3.53100528, -0.000123660988, -5.02999433e-07,  2.43530612e-09, -1.40881235e-12,     -1046.97628,      2.96747038],    # N2
    [      4.30179807,  -0.00474912097,  2.11582905e-05, -2.42763914e-08,  9.29225225e-12,      264.018485,       3.7166622],    # HO2
    [      4.31515149, -0.000847390622,  1.76404323e-05, -2.26762944e-08,  9.08950158e-12,     -17706.7437,      3.27373319],    # H2O2
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,      4.37967491],    # AR
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,     0.928723974],    # HE
    [        3.637266,     0.000185091,  -1.6761646e-06,    2.387202e-09,   -8.431442e-13,         50021.3,       1.3588605]     # OHEX
], dtype=np.float64)

# LOW NASA coefficients
a_high = np.array([
    #             a_1              a_2              a_3              a_4              a_5              a_6              a_7 
    [             2.5,             0.0,             0.0,             0.0,             0.0,        25473.66,     -0.44668285],    # H
    [      2.93286575,  0.000826608026, -1.46402364e-07,  1.54100414e-11,   -6.888048e-16,     -813.065581,     -1.02432865],    # H2
    [      2.54363697, -2.73162486e-05,  -4.1902952e-09,  4.95481845e-12, -4.79553694e-16,       29226.012,      4.92229457],    # O
    [      3.66096065,  0.000656365811, -1.41149627e-07,  2.05797935e-11, -1.29913436e-15,     -1215.97718,      3.41536279],    # O2
    [      2.83853033,   0.00110741289, -2.94000209e-07,  4.20698729e-11,  -2.4228989e-15,      3697.80808,      5.84494652],    # OH
    [       2.6770389,    0.0029731816,  -7.7376889e-07,   9.4433514e-11,  -4.2689991e-15,      -29885.894,         6.88255],    # H2O
    [      2.95257637,    0.0013969004, -4.92631603e-07,  7.86010195e-11, -4.60755204e-15,     -923.948688,      5.87188762],    # N2
    [      4.17228741,   0.00188117627, -3.46277286e-07,  1.94657549e-11,  1.76256905e-16,      31.0206839,      2.95767672],    # HO2
    [      4.57977305,   0.00405326003,  -1.2984473e-06,    1.982114e-10, -1.13968792e-14,     -18007.1775,     0.664970694],    # H2O2
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,      4.37967491],    # AR
    [             2.5,             0.0,             0.0,             0.0,             0.0,        -745.375,     0.928723974],    # HE
    [         2.88273,    0.0010139743,   -2.276877e-07,    2.174683e-11,   -5.126305e-16,         50265.0,        5.595712]     # OHEX
], dtype=np.float64)


"""________________________________Reaction constants________________________________"""
I = 32    # Number of reactions
# Pre-exponential factors [cm^3/mol/s v 1/s]
A = np.array([
      5071200000000000.0,           1255400.0,          13193000.0,             84999.0,          4.9806e+18,
      6165000000000000.0,           4.714e+18,          1.4818e+24,     4650000000000.0,           2123100.0,
        57734000000000.0,    32500000000000.0,      958400000000.0,      130000000000.0,  1604800000000000.0,
                214800.0,    24100000000000.0,          9.7543e+19,           9550000.0,     1740000000000.0,
        75900000000000.0,    15000000000000.0,     5930000000000.0,     2950000000000.0,      108000000000.0,
         6010000000000.0,     1310000000000.0,     1690000000000.0,           1450000.0,     2100000000000.0,
         2750000000000.0,     3230000000000.0
], dtype=np.float64)

# Temperature exponent [-]
b = np.array([
                -0.48596,             2.27039,             1.87803,             2.26419,            -1.21273,
                    -0.5,                -1.0,            -2.53792,                0.44,              2.1133,
                     0.0,                 0.0,             0.42008,                 0.0,                 0.0,
                  2.3219,                 0.0,            -1.92495,                 2.0,                 0.0,
                     0.0,                 0.0,                 0.5,                 0.5,                 0.5,
                     0.5,                 0.5,                 0.0,                 0.0,                 0.5,
                     0.5,                 0.5
], dtype=np.float64)

# Activation energy [cal/mol]
E = np.array([
              16126.6907,           6956.8844,           3150.9846,         -1784.78301,           612.03574,
                     0.0,                 0.0,           120.78576,                 0.0,         -1624.73016,
               171.02109,                 0.0,           -948.5938,         -1629.99571,          15549.4672,
             -3402.35997,          3970.00613,           9425.1358,          3970.00613,           317.99948,
              7269.00236,          5975.00835,          -859.99347,          -443.99515,         -1241.99422,
               -764.0015,          -167.00735,          4135.00661,                 0.0,          -477.99272,
              -968.00679,          -786.99109
], dtype=np.float64)


"""________________________________Reaction matrixes________________________________"""
# Forward reaction matrix
nu_forward = np.array([
    #   H   H2    O   O2   OH  H2O   N2  HO2 H2O2   AR   HE OHEX 
    [   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  0. H+O2=O+OH
    [   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  1. O+H2=H+OH
    [   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  2. OH+H2=H+H2O
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0],    #  3. 2OH=O+H2O
    [   2,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  4. 2H+M=H2+M
    [   0,   0,   2,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  5. 2O+M=O2+M
    [   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  6. O+H+M=OH+M
    [   1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  7. H+OH+M=H2O+M
    [   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  8. H+O2(+M)=HO2(+M)
    [   1,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    #  9. H+HO2=H2+O2
    [   1,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 10. HO2+H=2OH
    [   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 11. HO2+O=OH+O2
    [   0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0],    # 12. HO2+OH=H2O+O2
    [   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0],    # 13. 2HO2=H2O2+O2
    [   0,   0,   0,   0,   0,   0,   0,   2,   0,   0,   0,   0],    # 14. 2HO2=H2O2+O2
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0],    # 15. 2OH(+M)=H2O2(+M)
    [   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 16. H2O2+H=H2O+OH
    [   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 17. H2O2+H=H2+HO2
    [   0,   0,   1,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 18. H2O2+O=OH+HO2
    [   0,   0,   0,   0,   1,   0,   0,   0,   1,   0,   0,   0],    # 19. H2O2+OH=H2O+HO2
    [   0,   0,   0,   0,   1,   0,   0,   0,   1,   0,   0,   0],    # 20. H2O2+OH=H2O+HO2
    [   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0],    # 21. H+O+M=OHEX+M
    [   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   1],    # 22. OHEX+H2O=OH+H2O
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 23. OHEX+H2=OH+H2
    [   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1],    # 24. OHEX+N2=OH+N2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   1],    # 25. OHEX+OH=2OH
    [   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 26. OHEX+H=OH+H
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   1],    # 27. OHEX+AR=OH+AR
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 28. OHEX=OH+HV
    [   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1],    # 29. OHEX+O2=OH+O2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 30. OHEX+CO2=OH+CO2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1]     # 31. OHEX+CO=OH+CO
], dtype=np.float64)

# Backward reaction matrix
nu_backward = np.array([
    #   H   H2    O   O2   OH  H2O   N2  HO2 H2O2   AR   HE OHEX 
    [   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  0. H+O2=O+OH
    [   1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  1. O+H2=H+OH
    [   1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    #  2. OH+H2=H+H2O
    [   0,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0],    #  3. 2OH=O+H2O
    [   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],    #  4. 2H+M=H2+M
    [   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  5. 2O+M=O2+M
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    #  6. O+H+M=OH+M
    [   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0],    #  7. H+OH+M=H2O+M
    [   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    #  8. H+O2(+M)=HO2(+M)
    [   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],    #  9. H+HO2=H2+O2
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0],    # 10. HO2+H=2OH
    [   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0],    # 11. HO2+O=OH+O2
    [   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0],    # 12. HO2+OH=H2O+O2
    [   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0],    # 13. 2HO2=H2O2+O2
    [   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0],    # 14. 2HO2=H2O2+O2
    [   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0],    # 15. 2OH(+M)=H2O2(+M)
    [   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0],    # 16. H2O2+H=H2O+OH
    [   0,   1,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0],    # 17. H2O2+H=H2+HO2
    [   0,   0,   0,   0,   1,   0,   0,   1,   0,   0,   0,   0],    # 18. H2O2+O=OH+HO2
    [   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0],    # 19. H2O2+OH=H2O+HO2
    [   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0],    # 20. H2O2+OH=H2O+HO2
    [   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1],    # 21. H+O+M=OHEX+M
    [   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0],    # 22. OHEX+H2O=OH+H2O
    [   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    # 23. OHEX+H2=OH+H2
    [   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0],    # 24. OHEX+N2=OH+N2
    [   0,   0,   0,   0,   2,   0,   0,   0,   0,   0,   0,   0],    # 25. OHEX+OH=2OH
    [   1,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    # 26. OHEX+H=OH+H
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0],    # 27. OHEX+AR=OH+AR
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    # 28. OHEX=OH+HV
    [   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0],    # 29. OHEX+O2=OH+O2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0],    # 30. OHEX+CO2=OH+CO2
    [   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0]     # 31. OHEX+CO=OH+CO
], dtype=np.float64)

nu = nu_backward - nu_forward


"""________________________________Three-body reactions________________________________"""
ThirdBodyIndexes = np.array([   4,   5,   6,   7,   8,  15,  21], dtype=np.int64)
ThirdBodyCount = 7

# third-body efficiency factors
alfa = np.array([
    #       H       H2        O       O2       OH      H2O       N2      HO2     H2O2       AR       HE     OHEX 
    [     1.0,     2.5,     1.0,     1.0,     1.0,    12.0,     1.0,     1.0,     1.0,     1.0,    0.83,     1.0],    #  4. 2H+M=H2+M
    [     1.0,     2.5,     1.0,     1.0,     1.0,    12.0,     1.0,     1.0,     1.0,    0.83,    0.83,     1.0],    #  5. 2O+M=O2+M
    [     1.0,     2.5,     1.0,     1.0,     1.0,    12.0,     1.0,     1.0,     1.0,    0.75,    0.75,     1.0],    #  6. O+H+M=OH+M
    [     1.0,     2.5,     1.0,     1.0,     1.0,    12.0,     1.0,     1.0,     1.0,    0.38,    0.44,     1.0],    #  7. H+OH+M=H2O+M
    [     1.0,   1.511,     1.0,     1.0,     1.0,  11.372,     1.0,     1.0,     1.0,   0.474,    0.65,     1.0],    #  8. H+O2(+M)=HO2(+M)
    [     1.0,    2.47,     1.0,     0.8,     1.0,     5.0,     1.0,     1.0,    5.13,    0.67,    0.43,     1.0],    # 15. 2OH(+M)=H2O2(+M)
    [     1.0,     1.0,     1.0,     0.4,     1.0,     6.5,     0.4,     1.0,     1.0,    0.35,     1.0,     1.0]     # 21. H+O+M=OHEX+M
], dtype=np.float64)


"""________________________________Irreversible reactions________________________________"""
IrreversibleIndexes = np.array([], dtype=np.int64)
IrreversibleCount = 0


"""________________________________Pressure-dependent reactions________________________________"""
PressureDependentIndexes = np.array([   8,  15], dtype=np.int64)
PressureDependentCount = 2

LindemannIndexes = np.array([], dtype=np.int64)
LindemannCount = 0

# Fall-off parameters
ReacConst = np.array([
    #               A_0                b_0                E_0 
    [        5.2669e+19,          -1.37367,               0.0],    #  8. H+O2(+M)=HO2(+M)
    [        1.9928e+18,          -1.17797,          -2150.31]     # 15. 2OH(+M)=H2O2(+M)
], dtype=np.float64)

TroeIndexes = np.array([   8,  15], dtype=np.int64)
TroeCount = 2

# Troe parameters
Troe = np.array([
    #              alfa               T***                 T*                T** 
    [              0.67,             1e-30,             1e+30,             1e+30],    #  8. H+O2(+M)=HO2(+M)
    [              0.43,             1e-30,             1e+30,             1e+30]     # 15. 2OH(+M)=H2O2(+M)
], dtype=np.float64)

SRIIndexes = np.array([], dtype=np.int64)
SRICount = 0

# SRI parameters
SRI = np.array([], dtype=np.float64)

PlogIndexes = np.array([], dtype=np.int64)
PlogCount = 0

# PLOG parameters
Plog1 = np.array([], dtype=np.float64)

Plog2 = np.array([], dtype=np.float64)

Plog3 = np.array([], dtype=np.float64)
