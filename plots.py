import matplotlib.pyplot as plt
'''
n=int(input("enter the number of students"))
g=[]
for i in range(n):
    k=int(input("enter percent"))
    g.append(k)
plt.pie(g,labels=["a","b","c"],explode=[0,0.1,0])
plt.show()   
'''
x=[1,2,3,4]
y=[5,6,4,8]
plt.subplot(131)#dimension vs number of plot
plt.plot(y,x)
plt.subplot(132)
plt.plot(x,y)
plt.subplot(133)
plt.pie(y)
plt.plot()
plt.show()

