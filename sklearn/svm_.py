import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm,datasets
iris=datasets.load_iris()
x=iris.data[:,:2]
y=iris.target
#creating svm boundaries
x_min,x_max=x[:,0].min()-1,x[:,0].max()+1 #0 col in x
y_min,y_max=x[:,1].min()-1,x[:,0].max()+1 #1st col in y
h=(x_max/x_min)/100 #gap size
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max))
x_plot=np.c_[xx.ravel(),yy.ravel()] #creating control raven nd array ko flatten krta h
#set regularization param as 1
c=1.0 #C can vary from 0 to 1
svc_classifier=svm.SVC(kernel='linear',C=1.0) #creates model
svc_classifier=svc_classifier.fit(x,y) #fitting
z=svc_classifier.predict(x_plot) #prediction then testing of data
z=z.reshape(xx.shape)
plt.figure(figsize=(15,5))                  
plt.subplot(121)
plt.contour(xx,yy,z,cmap=plt.cm.tab10,alpha=0.3)#alpha for setting transparency
#customize graph
plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.Set1)
plt.xlabel('sepal-length')
plt.ylabel('petal-length')
plt.xlim(xx.min(),xx.max())
plt.title("Support Vector Classifier Linear Kernal")
svc_classifier=svm.SVC(kernel='rbf',gamma='auto',C=c).fit(x,y)
z=svc_classifier.predict(x_plot)
z=z.reshape(xx.shape)
plt.subplot(122)
plt.contour(xx,yy,z,cmap=plt.cm.tab10,alpha=0.3)
plt.scatter(x[:,0],x[:,1],c=y,cmap=plt.cm.Set1)
plt.xlabel('sepal-length')
plt.ylabel('petal-length')
plt.xlim(xx.min(),xx.max())
plt.title("Support Vector Classifier RBF Kernal")
plt.show()
