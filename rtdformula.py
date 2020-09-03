Rtres = 5000
Ra = 50
Vzero = 3
V = 6.5
print ((Rtres+Ra)*((1/(Vzero/V+1/2))-1)-Ra)
import numpy as np
To=298.2
Rt=2252
Ro=672.5
B=3940
T=(1/To + np.log(Rt/Ro)/B)
print (T-273)
