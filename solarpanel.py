import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
import matplotlib.pyplot as plt
df=pd.read_csv('SolarPrediction.csv',delimiter=',')
#df.drop_duplicates(subset=df,keep='first',inplace=True)
col=['Radiation','Temperature','TimeSunRise','TimeSunSet']
#df1=df[col][2:10]
##df['new']=df['TimeSunRise']-df['TimeSunSet']
##df['new']=df['new']/np.timedelta64(1,'m')
df.TimeSunRise=pd.to_datetime(df.TimeSunRise)
df.TimeSunSet=pd.to_datetime(df.TimeSunSet)
diff=df.TimeSunSet-df.TimeSunRise
diff=diff.drop_duplicates()
##print(diff)
plt.subplot(131)
plt.scatter(df.Time[:200],df.Radiation[:200],color='r')
plt.subplot(132)
plt.scatter(df.Time[:200],df.Temperature[:200],color='g')
diff=diff.reset_index()
newdiff=diff
newdiff[0].to_csv("nwe.csv")
plt.subplot(133)
plt.plot(newdiff[0],color='b')
plt.show()


##listt=[]
##out=open('out.csv','w')
##for diff in diff:
##    if diff not in listt:
##          listt.append(diff)
##        continue
##    else:
##        out.write(diff)
##        listt.append(diff)
##out.close()
##df3=pd.read_csv('out.csv',delimiter=',')
##print(listt)
        
  
