>>> import sklearn
>>> from sklearn import datasets
>>> iris=datasets.load_digits
>>> print(iris)
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
