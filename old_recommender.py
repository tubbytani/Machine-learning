import requests as rq
import bs4 as b
import re
import nltk
header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url='https://www.amazon.in/gp/product/B009BA7S8M/ref=pd_alm_al_1_1_na_dsk_sf_mw_img_bbsvd?fpw=alm&almBrandId=ctnow&pd_rd_r=34cb4ed3-1dc5-4557-89bc-842f45fe802e&pd_rd_w=bk2uE&pd_rd_wg=l2jjF&pd_rd_i=B009BA7S8M&pf_rd_r=FV45NYBTJHMTGS5KT3SK&pf_rd_p=d87d12f9-fc48-4de5-9378-793628da5ea8'
##page=rq.get(url,headers=header)
page=open('new.html','r')
soup=b.BeautifulSoup(page,'html.parser')
##html=list(soup.children)[1]
##body=list(html.children)[5]
reviews=soup.findAll('div',{'id':'customer_review-RVJ2YEP5RU2GC'})
cont=reviews[0].findAll('span')
review=list(cont[8])[0].lower()
sent_tokens=nltk.sent_tokenize(review)
word_tokens=nltk.word_tokenize(review)
review=review.split()
lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(token):
    return[lemmer.lemmatize(token) for token in tokens] #converts into original word token 
#remove_punct=dict((ord(punct),None)for punct in string.punctuation)
remove_punct=[word for word in word_tokens if word.isalnum()]
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(remove_punct))
good_comment=['Ok','Useful','productive','good']
bad_comment=['worse','foul','not good','smell','hate']
print(word_tokens)
countgood=0
countbad=0
for comment in review:
    for n in good_comment:
        if comment==n:
            countgood+=1
    for m in bad_comment:
        if comment==m:
            countbad+=1
'''
check if word from good_comment or bad_comment is in the usercoment. If count(goodcomment)>count(badcomment): say article is good
otherwise article is bad
'''
if countgood>countbad:
    print('Article is good')
else:
    print('Article is bad')
#sent_tokens=nltk.sent_tokenize(review)
