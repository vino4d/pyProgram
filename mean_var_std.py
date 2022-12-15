#calculate mean, variance, standard deviations
#For 3*3 matrix that given by user

import numpy as np
a=input()
a=a.split(',')
a=[int(i) for i in a]
if len(a)!=9:
    raise ValueError( "List must contain nine numbers.")
a=np.array(a)
a=a.reshape(3,3)

mean=[]
var=[]
sd=[]
min=[]
max=[]
sum=[]

#calc fun to do np.func(f) with input val(v)
def calculate(x,v,f):
    x.append(list(f(v,axis=0)))
    x.append(list(f(v,axis=1)))
    x.append(f(v))

calculate(mean,a,np.mean)
calculate(var,a,np.var)
calculate(sum,a,np.sum)
calculate(sd,a,np.std)
calculate(min,a,np.min)
calculate(max,a,np.max)

ans={'mean':mean,'variance':var,'standard deviation':sd,'min':min,'max':max,'sum':sum}
print(ans)
