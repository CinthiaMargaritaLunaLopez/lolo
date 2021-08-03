import numpy as np

x=np.array([1,2,3,4,5,7,8,8,10])
y=np.array([7,8,8,10,9,8,11,10,8,11])

px=np.mean(x)
py=np.mean(y)

num=np.sum((x-px)*(y-py))
den=np.sum(x*(x-px))
pendiente= num/den

constante=py-pendiente*px

print ("y= {} + {}*x".format(constante,round(pendiente,4)))

print(pendiente)
print(constante)