
import math
import random
import numpy as np
import pandas as pd


#Creates list with Laplace noise (uses builtin function)
#Parameters: scale and size
def Laplace(scale,n):
    m=0
    sample = np.random.laplace(m, scale, n)
    listN = []
    for x in range(1000):
        listN.append(sample[x])
    return listN
   

#Creates list with Laplace noise
#Parameters: a dict and the epsilon
def Laplacem(dic,epsilon):
     #sensitivity
    try:
       values=[]
       for x in dic:
          values.append(dic[x])
       maxi = max(values)
       mini = min(values)
    except ValueError or TypeError:
        maxi = dic.max()
        mini = dic.min()   
    sigma = (maxi - mini)/epsilon
    
   #Generating random variables according to the Laplace distribution
    x = np.random.random_sample((2000,))
    l=[]
    for i in range(len(dic)):
       if x[i]<1/2:
          noise = (sigma/math.sqrt(2))*math.log(2*x[i])
       else:
          noise = -(sigma/math.sqrt(2))*math.log(2*(1-x[i]))
       l.append(noise)
    return l

#df = readdata()
#data = df["ONOMA"]
#count = Counter(data)
#print Laplace(2,200)
#print "\n"
#print Laplacem(count,20)

