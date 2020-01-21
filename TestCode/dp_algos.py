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
    for x in range(1327):
        listN.append(sample[x])
    return listN
   

#Creates list with Laplace noise
#Parameters: a dict and the epsilon
def Laplacem(dic,epsilon):

   #sensitivity
   values=[]
   for x in dic:
      values.append(dic[x])
   maxi = max(values)
   mini = min(values)

   #Generating random variables according to the Laplace distribution
   sigma = (maxi - mini)/float(epsilon)
   x = np.random.random_sample((2000,))
   l=[]
   for i in range(len(dic)):
      if x[i]<1/2:
         noise = (sigma/math.sqrt(2))*math.log(2*x[i])
      else:
         noise = -(sigma/math.sqrt(2))*math.log(2*(1-x[i]))
      l.append(noise)
   return len(l)


#Creates list with Laplace noise
#Parameters: a list and the epsilon
def Laplacel(dic,epsilon):
  
    #sensitivity    
    maxi = dic.max()
    mini = dic.min()
   
    #Generating random variables according to the Laplace distribution
    sigma = (maxi - mini)/(float(epsilon)*len(dic))
    x = np.random.random_sample((2000,))
    l=[]
    for i in range(len(dic)):
       if x[i]<1/2:
          noise = (sigma/math.sqrt(2))*math.log(2*x[i])
       else:
          noise = -(sigma/math.sqrt(2))*math.log(2*(1-x[i]))
       l.append(noise)
    return l


def histo (data, epsilon):  
    se = data["BATHMOS"]
    n = len(se)
    l = Laplace(n, epsilon)
    l=pd.Series(l)
    #print l
    se2 = se +l
    #se = pd.DataFrame(se, columns = ['one'])
    #se['two']=se['one'] 
    df = pd.concat([se, se2], axis=1)
    df.columns =  ["original data", "data with noise (e=0.01) "]
    print df
    df.plot.hist(bins=120, alpha=0.6, figsize=(11,6))


