#23.05.2017, Michael Meindl
#Batch Fitting different SISO-Functions using polynomial models


import numpy as NP
import numpy.linalg as LA
import matplotlib.pyplot as PLT

M  = 5;
N  = 2000;
dx = 3.0 / N;
x  = [dx*k for k in range(N)]

#Custom noise
offset = 0;
e  = (NP.random.rand(N)*offset*2).tolist();
#First Target function aka sinus
y1 = NP.sin(x);
t1 = y1 + e - offset;
#Second Target function aka e^x
y2 = NP.exp(x)
t2 = y2 + e - offset;
#Second Target function aka x^2
y3 = NP.power(x, 2)
t3 = y3 + e - offset;

#Fit first model
PhiMat = NP.empty( (N, M) )
for i in range(N):
    for j in range(M):
        PhiMat[i][j] = x[i]**j
w1 = LA.inv(PhiMat.T.dot(PhiMat)).dot(PhiMat.T).dot(t1)
w2 = LA.inv(PhiMat.T.dot(PhiMat)).dot(PhiMat.T).dot(t2)
w3 = LA.inv(PhiMat.T.dot(PhiMat)).dot(PhiMat.T).dot(t3)

m1 = [0 for k in range(N)]
m2 = [0 for k in range(N)]
m3 = [0 for k in range(N)]

for k in range(N):
    m1[k] = w1[0] + w1[1]*(x[k]**1) + w1[2]*(x[k]**2) + w1[3]*(x[k]**3) + w1[4]*(x[k]**4)
    m2[k] = w2[0] + w2[1]*(x[k]**2) + w2[2]*(x[k]**2) + w2[3]*(x[k]**3) + w2[4]*(x[k]**4)
    m3[k] = w3[0] + w3[1]*(x[k]**2) + w3[2]*(x[k]**2) + w3[3]*(x[k]**3) + w3[4]*(x[k]**4)
    
PLT.figure()
PLT.plot(x, t1, label="Measured Value")
PLT.plot(x, y1, label="Targeted Model")
PLT.plot(x, m1, label="Model Values")
PLT.legend()
PLT.grid(True)
PLT.title('Sinus-Function')
PLT.show()

PLT.figure()
PLT.plot(x, t2, label="Measured Value")
PLT.plot(x, y2, label="Targeted Values")
PLT.plot(x, m2, label="Model Values")
PLT.legend()
PLT.grid(True)
PLT.title('e-Function')
PLT.show()

PLT.figure()
PLT.plot(x, t3, label="Measured Value")
PLT.plot(x, y3, label="Targeted Values")
PLT.plot(x, m3, label="Model Values")
PLT.legend()
PLT.grid(True)
PLT.title('X-Squared-Fucntion')
PLT.show()