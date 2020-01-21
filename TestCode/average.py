from dp_algos import Laplace
from dp_algos import Laplacel

#Returns the average BATHMOS of poeople 
def av_query(data):
    df = data
    #df = data[data.TRITEKNOS=="YES"]
    df = df["BATHMOS"]
    mesos = df.mean()
    return mesos


#WITH Differential Privacy
def dpav_query (data, data2, epsilon):
    df2 = data2
    #df = data2[data2.TRITEKNOS=="YES"]
    df2 = df2["BATHMOS"]
    df = data["BATHMOS"]
    #generate Laplace_noise
    l=Laplacel(df, epsilon)
    #print l
    m=sum(l)/len(l)
    mesos = df2.mean() + m
    return mesos


