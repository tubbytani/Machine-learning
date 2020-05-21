import numpy
import pandas as pd
import matplotlib.pyplot as plt
url="https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv"
'''
url4="https://raw.githubusercontent.com/Godoy/imdb-5000-movie-dataset/master/data/movie_metadata.csv"
df2=pd.read_csv(url4,delimiter=',')
df2.to_csv('movies.csv')
'''
df=pd.read_csv(url,delimiter=',')
df1=df["sepal_length"][2:50]
df0=df["petal_length"][2:50]
#print(df0)
#print(df1)
#plt.plot(df1,df0)
#plt.show()
#print(df1.head(2))
plt.bar(df1,df0)
plt.show()

'''
dct={'hi':["ok","h"],'hj':["kl","l"]}
df2=pd.DataFrame(dct)
print(df2)
#df.to_csv("filepath.txtor csv") converts url to csv
'''
