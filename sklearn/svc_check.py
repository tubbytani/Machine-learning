<function load_digits at 0x000001224CE6AEE8>
>>> iris=datasets.load_digits()
>>> type(iris)
<class 'sklearn.utils.Bunch'>
>>> digit=datasets.load_digits()
>>> digit.target
array([0, 1, 2, ..., 8, 9, 8])
>>> for dat in digit.target:
	#print dat
	break

>>> clf=svm.Svc(gamma=0.01,c=100.)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    clf=svm.Svc(gamma=0.01,c=100.)
NameError: name 'svm' is not defined
>>> import sklearn as svm
>>> clf=svm.Svc(gamma=0.01,c=100.)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    clf=svm.Svc(gamma=0.01,c=100.)
AttributeError: module 'sklearn' has no attribute 'Svc'
>>> clf=svm.SVC(gamma=0.01,c=100.)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    clf=svm.SVC(gamma=0.01,c=100.)
AttributeError: module 'sklearn' has no attribute 'SVC'
>>> from sklearn import svm
>>> clf=svm.SVC(gamma=0.01,c=100.)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    clf=svm.SVC(gamma=0.01,c=100.)
  File "C:\Users\new\AppData\Local\Programs\Python\Python37\lib\site-packages\sklearn\utils\validation.py", line 73, in inner_f
    return f(**kwargs)
TypeError: __init__() got an unexpected keyword argument 'c'
>>> clf=svm.SVC(gamma=0.01,C=100.)
>>> clf.fit(digit.data[:-1],digit.target[:-1])
SVC(C=100.0, gamma=0.01)
>>> 
