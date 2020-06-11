import pandas as pd
import datetime
from datetime import date
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import datetime
from datetime import date
df=pd.read_csv('SolarPrediction.csv',delimiter=',')
uniq='df'
#df.drop_duplicates(subset=uniq,keep='first',inplace=True)
col=['Radiation','Temperature','TimeSunRise','TimeSunSet']

df.TimeSunRise=pd.to_datetime(df.TimeSunRise)
df.TimeSunSet=pd.to_datetime(df.TimeSunSet)
diff=df.TimeSunSet-df.TimeSunRise
diff=diff.drop_duplicates()
##print(diff)
##plt.subplot(131)
##lst=[1,5,10]
##plt.xticks(ticks=lst)
##plt.title("radiation vs time")
##plt.scatter(df.Time[:200],df.Radiation[:200],color='r')
##plt.subplot(132)
##plt.title("temperature vs time")
##lst=[1,5,10]
##plt.xticks(ticks=lst)
##plt.scatter(df.Time[:200],df.Temperature[:200],color='g')
diff=diff.reset_index()
newdiff=diff
newdiff[0].to_csv("kl.csv")
##print(diff)
plt.subplot(133)
lst=[1,5,10]
plt.xticks(ticks=lst)
#plt.plot(newdiff[0],color='b')



l=[]
for i in range(75):
               k=(diff[0][i].value)/10000000000
               l.append(k)
col=["date","solar"]
col2=["date"]
from sklearn.linear_model import LogisticRegression
new=pd.read_csv("nwe.csv",names=col)
X=new[col2]
y=l   
clf = LogisticRegression(random_state=0).fit(X, y)
print(X)
print("predict")
#print(clf.predict(X))
print(clf.predict_proba(X))
print("score")
print(clf.score(X, y))
##----2nd model
from sklearn.linear_model import LinearRegression
Z=new[col2]
n=l   
clf = LinearRegression().fit(Z, n)
print(Z)
print("predict")
print(clf.predict(Z))
#print(clf.predict_proba(Z))
print("score")
print(clf.score(Z, n))

