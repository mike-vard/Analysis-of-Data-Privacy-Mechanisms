import pandas as pd
import numpy as np
import random as rd
import matplotlib as mlt
import average as av
from collections import Counter


#read csv file
#data = pd.read_csv('/Users/mikevard/Desktop/PYTHON-DP/student-mat.csv', sep = ';')
data = pd.read_csv('/Users/mikevard/Desktop/PYTHON-DP/PE19CSV2.csv', sep = ';')

df = data["TRITEKNOS"]
n=o=0
for item in df:
    if item == "YES":
        n+=1
    else:
        o+=1
print "YES: ",n , ", NO: ", o 




#se.hist(bins=80)



#shows a quick statistic summary of your data:
#print data.describe()

#print data["sex"]
#print data.get_dtype_counts()
#print data.dtypes
#print data.values

#select
#print data.loc[38]
#print data.iloc[38]
#df = data.loc[5:38,["sex","school"]]
#df = data.loc[(data["sex"]=="F"),["sex"]]
#df = data.loc[5:355,["age"]]

#filtering
#df = data[data.age>19]
#df = data.query('(age > 18) & (G1==9)') 
#df = data[data["age"].isin(['18','22'])]





#print "%.2f" % av.av_query(data)
print "%.2f" % av.dpav_query (data, data, 0.01)




#write file
#data.to_csv("f.csv")

