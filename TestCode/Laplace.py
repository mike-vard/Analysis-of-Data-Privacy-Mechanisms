
import math
import random
import numpy as np
import pandas as pd


#Creates list with Laplace noise (uses builtin function)
#Parameters: scale and size

   

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

def Laplace(n,e):
    m=0
    scale = 4.8/float(n*e)
    sample = np.random.laplace(m, scale, n)
    listN = []
    for x in range(1327):
        listN.append(sample[x])
    return listN

def dpav_query (data, epsilon):
    #df = data2[data2.TRITEKNOS=="YES"]
    
    df = data["BATHMOS"]
    #generate Laplace_noise
    n = len(df)
    l=Laplace(n, epsilon)
    print l
    m=sum(l)/len(l)
    mesos = df.mean() + m
    return mesos


data = pd.read_csv('/Users/mikevard/Desktop/PYTHON-DP/PE19CSV2.csv', sep = ';') 
d5 = data[data.BATHMOS==5.0]
se = data["BATHMOS"]
data2 = data
n = len(se)
l = Laplace(n, 0.05)
l=pd.Series(l)
se2 = se +l

df = pd.concat([se, se2], axis=1)
df.columns =  ["original data", "data with noise (e=0.1) "]
#print df
#df.plot.hist(bins=120, alpha=0.6, figsize=(11,6))
data2.BATHMOS  = se2






#df = readdata()
#data = df["ONOMA"]
#count = Counter(data)
#print Laplace(2,200)
#print "\n"
#print Laplacem(count,20)

