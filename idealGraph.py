import matplotlib.pyplot as plt
import numpy as np 
x=np.linspace(0,5,100)
b=1-x
c=x
a=x

fig,(p,q,r)=plt.subplots(1,3,figsize=(10,5))
p.plot(b,x,'r',lw=3)
p.set(title="Boyle's Law",xlabel="V",ylabel="P")
q.plot(c,x,'g',lw=3)
q.set(title="Charles' Law",xlabel="T",ylabel="V")
r.plot(a,x,lw=3)
r.set(title="Avogadro's Law",xlabel="n",ylabel="V")
plt.show()