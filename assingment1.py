
import requests
import re
from bs4 import BeautifulSoup
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


nltk.download('stopwords')
nltk.download('wordnet')



## extracting the data from the website 
page =requests.get('https://en.wikipedia.org/wiki/Natural_language_processing')
src= page.content
soup= BeautifulSoup(src,'lxml')
text= ''.join([ p.text for p in soup.find_all('p')])


## cleaning the data
cleaned_data= re.sub(r'[^\w\s]','',text)

## Normalization
normatized_text= cleaned_data.lower()

## Tokenization 

tokenized_text= normatized_text.split()


## Lemmatization

lemm= WordNetLemmatizer()

lemmatized_text = [lemm.lemmatize(word) for word in tokenized_text]



## Unique Words


stop_words = set(stopwords.words('english'))

unique_words= [word for word in lemmatized_text if word not in stop_words]

# print(unique_words)

for word in unique_words:
    if len(word) <3 :
        print(word)















