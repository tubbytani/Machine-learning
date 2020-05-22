import requests as rq
import bs4 as b
import re
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url1="https://www.amazon.in/HP-eq0007au-15-6-inch-Windows-Graphics/dp/B08496K8JL/ref=sr_1_1_sspa?dchild=1&keywords=laptop+hp&qid=1590123379&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRERNWTNMNjNOS0k5JmVuY3J5cHRlZElkPUEwNzI0OTI3MTkzTjA1NDg3OVgxQyZlbmNyeXB0ZWRBZElkPUEwNDYwMzY1MTdENjQ1Q1ZCNUdSTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
url3="https://www.amazon.in/HP-14-inch-Laptop-Windows-cs0017TU/dp/B07S5VRTK9/ref=sr_1_9?dchild=1&keywords=laptop+hp&qid=1590123379&sr=8-9"
page=rq.get(url3,headers=header)
#print(page.status_code)
soup=b.BeautifulSoup(page.content,'html.parser')
##body=list(html.children)[4]
reviews=[]
##reviews=soup.findAll("span",{"data-hook":"review-body"})

for i in soup.findAll("span",{"data-hook":"review-body"}): #refines the search
            reviews.append(i.text)#converts html codes into readable text 
reviews=str(reviews).lower()            
reviews=re.sub(r'[^\w\s]',' ',str(reviews))
reviews=re.sub("/[^A-Z0-9]/ig",' ',str(reviews))
print(reviews)
usercomment=reviews.split()
#print(usercomment)
good_comment=['pretty','good','slim','cheap','fast']
bad_comment=['glare','not ok','bad','useless','slow']
count=0
count1=0
for j in range(len(usercomment)):
    for i in range(len(good_comment)):
        if good_comment[i]==usercomment[j]:
            count+=1
    for i in range(len(bad_comment)):
        if bad_comment[i]==usercomment[j]:
            count1+=1            
 
##print(count)
##print(count1)

if count>count1:
        print("review is good")
else:
        print("review is bad")
