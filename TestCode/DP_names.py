import numpy as np
import random as rd
import pandas as pd
import matplotlib.pyplot as plt
import dp_algos as a
from collections import Counter

#Read data set 
def readdata():
   #add=raw_input("Give file name:")
   add='PE19CSV2'
   path='/Users/mikevard/Desktop/PYTHON-DP/'+add+'.csv'
   df = pd.read_csv(path, sep=';')
   return df

 
#Generates a data set that differs in one element 
#from original data set
def falsedata(df):
    
    data = df
    n = len(data)
    #random name
    names = data["ONOMA"]
    i = rd.randint(0, n)
    rdname = names.loc[i]
    #random moria
    maxm = data["MORIA"].max()
    minm = data["MORIA"].min()
    rdmoria = "%.3f" % rd.uniform(minm, maxm)
    #random vathmos
    maxb = data["BATHMOS"].max()
    minb = data["BATHMOS"].min()
    rdbathmos = "%.3f" % rd.uniform(minb, maxb)
    
    #random triteknos, with probability
    cbool = Counter(data["TRITEKNOS"])
    p1 = cbool['YES']/float(n)
    p2 = cbool['NO']/float(n)
    rdtrit = np.random.choice(["YES", "NO"], size=None, p=[p1, p2])
   
     #random paidagogiko, with probability   
    cbool = Counter(data["PAIDAGOGIKO"])
    p1 = cbool['YES']/float(n)
    p2 = cbool['NO']/float(n)
    rdpaid = np.random.choice(["YES", "NO"], size=None, p=[p1, p2])
    
    i = rd.randint(0, n)
    data.loc[i] = [rdname, rdmoria, rdpaid, rdbathmos, rdtrit ]
    return data


def add_noise(data,e):
    n=len(data)
    #lapN = Laplace(2, n)
    count = Counter(data)
    lapN = a.Laplace(1/float(e), n)
    
    #print "Most common names, initialy:", count.most_common(3)
    test = count.most_common(12)
    x=[]
    y=[]
    for i in range(12):
        x.append(test[i][0])
        y.append(test[i][1])
    print "intially:"
    plt.barh(x,y, color='darkblue')
    plt.show()
    i=0
    for item in count:
        #print i, "   ", item , "\n"
        count[item]+=lapN[i]
        i+=1
    
    #print "Most common names, finally:", count.most_common(3)
    
    test = count.most_common(12)
    x=[]
    y=[]
    for i in range(12):
        x.append(test[i][0])
        y.append(test[i][1])
    print "fianally:"
    plt.barh(x,y, color='darkblue')
    plt.show()
    
    
def add_noisem(data,e):
    n=len(data)
    #lapN = Laplace(2, n)
    count = Counter(data)
    lapN = a.Laplacem(count, n)
    #print "Initial: ", count
    print "Most common names, initialy:", count.most_common(1)
    i = 0
    for item in count:
        #print i, "   ", item , "\n"
        count[item]+=lapN[i]
        i+=1
    
    print "Most common names, finally:", count.most_common(1)
    
   


df = readdata()
data = df["ONOMA"]
add_noise(data,1)





