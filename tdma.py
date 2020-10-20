import numpy as np

# Given Variable
DX = 0.25

mL = 2
D = 2 + (mL*2)(DX**2)
# m is number of points
m = 4
# theta is unknown
theta_TDMA = np.zeros(m)

# #  TDMA
b = np.zeros(m)
a = np.zeros(m)
c = np.zeros(m)
d = np.zeros(m)

a[1:m-1]= -1
a[m-1]=-2
b[:]=D
c[0:m-1]=-1
d[0]=1

gamma = np.zeros(m)
beta = np.zeros(m)
beta[0]=b[0]
gamma[0]=d[0]/beta[0]

for i in range(1,m):
    	
    beta[i] = (b[i] - (a[i]*c[i-1])/beta[i-1])
    gamma[i] = d[i] - (a[i]*gamma[i-1])/beta[i]

    
theta_TDMA[m-1]=gamma[m-1]

for k in range(m-2,-1,-1):
    
    theta_TDMA[k] = gamma[k] - (c[k]*theta_TDMA[k+1])/beta[k]

print(theta_TDMA)