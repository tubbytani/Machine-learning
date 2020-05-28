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
url="https://raw.githubusercontent.com/venky14/Machine-Learning-with-Iris-Dataset/master/Iris.csv"
cols=['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Species']
pima=pd.read_csv(url)
print(pima.head())
feature_cols=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
x=pima[feature_cols]
y=pima.Species
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
dot_data=export_graphviz(clf,out_file=None,filled=True,rounded=True,special_characters=True,feature_names=feature_cols,class_names=['Iris-setosa','Iris-versicolor','Iris-virginica'])
graph=pdp.graph_from_dot_data(dot_data) 
graph.write_png('Iris.png')
Image(graph.create_png())
