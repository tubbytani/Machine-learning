'''Advanced recommender using nltk and bs4'''
'''Advancement in chatbot'''
import requests as rq
import bs4 as b
import re
import nltk #natural language toolkit
from sklearn.feature_extraction.text import TfidfVectorizer #sklearn module to process tfidfcalculation
from sklearn.metrics.pairwise import cosine_similarity #sklearn module to process cosine similarity
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url='https://www.amazon.in/gp/product/B009BA7S8M/ref=pd_alm_al_1_1_na_dsk_sf_mw_img_bbsvd?fpw=alm&almBrandId=ctnow&pd_rd_r=34cb4ed3-1dc5-4557-89bc-842f45fe802e&pd_rd_w=bk2uE&pd_rd_wg=l2jjF&pd_rd_i=B009BA7S8M&pf_rd_r=FV45NYBTJHMTGS5KT3SK&pf_rd_p=d87d12f9-fc48-4de5-9378-793628da5ea8'
page=rq.get(url,headers=header)
page=open('new.html','r')
soup=b.BeautifulSoup(page,'html.parser')
####html=list(soup.children)[1]
####body=list(html.children)[5]
reviews=soup.findAll('div',{'id':'customer_review-RVJ2YEP5RU2GC'})
cont=reviews[0].findAll('span')
review=list(cont[8])[0].lower()
##file=open('chatbot.txt','r')
##review=file.read()
lemmer=nltk.stem.WordNetLemmatizer()
word_tokens=nltk.word_tokenize(review)
sent_tokens=nltk.sent_tokenize(review)
def LemTokens(token): # function used for lemmatization
    return [lemmer.lemmatize(token) for token in tokens]
remove_puct = [word for word in word_tokens if word.isalnum()]
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(remove_puct))


import random
greetings=['hi','hello','hola','namste','hey']
response=['hello','hey','ram ram','jai mata di','to kaise hain aap log']


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in greetings:
            return random.choice(word_tokens)

### Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english') #n/N 1+log(N/n)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
##
##
flag=True
print("Robot: Hello.. Shaktiman")
##
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("Push:  You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("Push:  "+greeting(user_response))
            else:
                print("Push:  ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
print("Push:  Bye! take care..")

