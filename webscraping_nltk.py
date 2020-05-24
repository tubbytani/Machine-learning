import requests as rq
import bs4 as b
import re
import nltk
from nltk.corpus import wordnet
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url3="https://www.amazon.in/HP-14-inch-Laptop-Windows-cs0017TU/dp/B07S5VRTK9/ref=sr_1_9?dchild=1&keywords=laptop+hp&qid=1590123379&sr=8-9"
page=rq.get(url3,headers=header)
#print(page.status_code)
soup=b.BeautifulSoup(page.content,'html.parser')
##body=list(html.children)[4]
reviews=[]
lemmatized=[]
for i in soup.findAll("span",{"data-hook":"review-body"}): #refines the search
            reviews.append(i.text.split())#converts html codes into readable text 
reviews=re.sub(r'\b\d+\b','',str(reviews)) #removing numbers
reviews=re.sub(r'[^\w\s]','',str(reviews))
reviews=str(reviews).lower()
reviews=nltk.word_tokenize(str(reviews)) #word_token
##reviews=[word for word in reviews if word.isalpha()]
##print(reviews[:100])
lemmer=nltk.stem.WordNetLemmatizer()
def lemtoken(token):
    return lemmer.lemmatize(token,pos='a') #adjective
for i in reviews:
    lemmatized.append(lemtoken(i))
#print(lemmatized)
good=['pretty','good','slim','cheap','fast','durable']#sample text1
bad=['glare','not ok','bad','useless','slow','weak']    #sample text2
good_comment=[]
bad_comment=[]
def syn(word):#making synonyms
    for j in wordnet.synsets(word):
        for l in j.lemmas():
            good_comment.append(l.name())
def ant(word):#making antonyms           
    for j in wordnet.synsets(word):
        for l in j.lemmas():
            bad_comment.append(l.name())
for i in good:
    syn(i)
for i in bad:
    ant(i)
good_comment+=good
bad_comment+=bad
count=0
count1=0
#print(bad_comment)
for j in range(len(reviews)):
    for i in range(len(good_comment)):
        if good_comment[i]==reviews[j]:
            count+=1
    for i in range(len(bad_comment)):
        if bad_comment[i]==reviews[j]:
            count1+=1            
#if we could separate only the adjectives from review
print("The most common review word is: ",nltk.FreqDist(reviews).least_common(10))
print("The good review count is: ",count)
print("the bad review count is: ",count1)

if count>count1:
        print("review is good")
else:
        print("review is bad")
