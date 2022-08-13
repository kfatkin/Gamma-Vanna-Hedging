import numpy as np
from scipy.stats import norm
def delta(flag, s, k, t, r, v):
    d1 = (np.log(s/k)+(r+v*v/2)*t)/(v*np.sqrt(t))
    if flag == 'C':
        return norm.cdf(d1)
    else:
        return norm.cdf(-d1) # +signed put delta

Type = 'C' # call
S = 97.65 # underlying
K = 100.00 # strike
T = 30/365 # 30 days to expiry (in years)
R = 0.00 # “risk-free” rate
V = 0.12 # 12 vol
print(delta(Type, S, K, T, R, V))
