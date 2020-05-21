import requests as rq
import bs4 as b
page=rq.get("https://lipsum.com/")
#print(page.content)#prints html content but it looks bad
soup=b.BeautifulSoup(page.content,'html.parser')
#soup=soup.prettify()#to make it look better--converts into string so.children wont work
#print(soup)

##body=list(html.children)[4]
#child=list(soup.children) #printing all child
##print(child)
html=list(soup.children)[2]#soup se html m extract 2nd pos pe h html
body=list(html.children)[3]#html k andar body use extractkr liya
p=body.findAll('p')[0].get_text() #at 0th position
#para=list(p)
#p.split() #words are separated
#print(p)
##for i in p:
##    conts=list(i.children)
##    prints(conts)

#for movie review
p=p.replace(',','')
p=p.replace('.','') #replaces in original
usercomment=p.lower().split()
print(usercomment)
good_comment=['Lorem','ipsum','industry','more']
bad_comment=['worse','not ok','grow up','rethink']
count=0
count1=0
for j in range(len(usercomment)):
    for i in range(len(good_comment)):
        if good_comment[i]==usercomment[j]:
            count+=1
    for i in range(len(bad_comment)):
        if bad_comment[i]==usercomment[j]:
            count1+=1            
 
if count>count1:
        print("article is good")
else:
        print("article is bad")

#useless
##file=open('mylocalpage.html','w')
##file.write(soup)
##file.close()
'''

