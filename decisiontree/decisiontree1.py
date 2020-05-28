from sklearn import svm,datasets
from sklearn.cluster import KMeans
from pylab import *
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pydotplus as pdp
from IPython.display import Image
##iris=datasets.load_iris()
##x,y=iris.data,iris.target#x[:0] is the first coloumn
##k_means=KMeans(n_clusters=3,random_state=0)
###cluster is for taken data is in divided in three groups
##k_means.fit(x)
##y_pred=k_means.predict(x)
##scatter(x[:,0],x[:,1],c=y_pred)
##show()
url="https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
cols=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima=pd.read_csv(url,header=None,names=cols)
print(pima.head())
feature_cols=['pregnant','age','insulin','bmi','glucose','pedigree','bp']
x=pima[feature_cols]
y=pima.label
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
clf=DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)
result=confusion_matrix(y_test,y_pred)
print("confusion matrix")
print(result)
result1=classification_report(y_test,y_pred)
print("classification report")
print(result1)
result2=accuracy_score(y_test,y_pred)
print("accuracy: ",result2)
dot_data=export_graphviz(clf,out_file=None,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,class_names=['0','1'])
graph=pdp.graph_from_dot_data(dot_data) 
graph.write_png('Tree.png')
Image(graph.create_png())
