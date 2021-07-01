
# !pip install flask-restful
# !pip install flask_cors
print("Initializing!")
from flask_cors import CORS

import flask
from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import warnings, re,math, datetime, time
start_time = time.time()
from datetime import timedelta
# !pip install flask-ngrok
warnings.filterwarnings("ignore")
import math
import pandas as pd
import csv, io
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt
import nltk, string
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import SnowballStemmer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from geopy import geocoders
gn = geocoders.GeoNames(username = "idselection")
import shapely
from shapely.geometry import Point, LineString, Polygon
from flask import request
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import scipy.spatial

print("Loading Model!")
module_url="https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("Model Loaded!")
import nltk



nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")


from flask import Flask
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
CORS(app)
run_with_ngrok(app)   

from nltk.stem import WordNetLemmatizer

api = Api(app)


def clean(text):
      lemmatizer = WordNetLemmatizer()
      stemmer = SnowballStemmer('english')
      vectorizer = TfidfVectorizer(use_idf = True, tokenizer = nltk.word_tokenize,stop_words='english', smooth_idf = True)
      remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
      stopw = set(stopwords.words('english'))
      contraction = {"ain't": "is not", "aren't": "are not","can't": "cannot", 
                      "can't've": "cannot have", "'cause": "because", "could've": "could have", 
                      "couldn't": "could not", "couldn't've": "could not have","didn't": "did not", 
                      "doesn't": "does not", "don't": "do not", "hadn't": "had not", 
                      "hadn't've": "had not have", "hasn't": "has not", "haven't": "have not", 
                      "he'd": "he would", "he'd've": "he would have", "he'll": "he will", 
                      "he'll've": "he he will have", "he's": "he is", "how'd": "how did", 
                      "how'd'y": "how do you", "how'll": "how will", "how's": "how is", 
                      "I'd": "I would", "I'd've": "I would have", "I'll": "I will", 
                      "I'll've": "I will have","I'm": "I am", "I've": "I have", 
                      "i'd": "i would", "i'd've": "i would have", "i'll": "i will", 
                      "i'll've": "i will have","i'm": "i am", "i've": "i have", 
                      "isn't": "is not", "it'd": "it would", "it'd've": "it would have", 
                      "it'll": "it will", "it'll've": "it will have","it's": "it is", 
                      "let's": "let us", "ma'am": "madam", "mayn't": "may not", 
                      "might've": "might have","mightn't": "might not","mightn't've": "might not have", 
                      "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", 
                      "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", 
                      "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not",
                      "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", 
                      "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", 
                      "she's": "she is", "should've": "should have", "shouldn't": "should not", 
                      "shouldn't've": "should not have", "so've": "so have","so's": "so as", 
                      "this's": "this is",
                      "that'd": "that would", "that'd've": "that would have","that's": "that is", 
                      "there'd": "there would", "there'd've": "there would have","there's": "there is", 
                      "they'd": "they would", "they'd've": "they would have", "they'll": "they will", 
                      "they'll've": "they will have", "they're": "they are", "they've": "they have", 
                      "to've": "to have", "wasn't": "was not", "we'd": "we would", 
                      "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", 
                      "we're": "we are", "we've": "we have", "weren't": "were not", 
                      "what'll": "what will", "what'll've": "what will have", "what're": "what are", 
                      "what's": "what is", "what've": "what have", "when's": "when is", 
                      "when've": "when have", "where'd": "where did", "where's": "where is", 
                      "where've": "where have", "who'll": "who will", "who'll've": "who will have", 
                      "who's": "who is", "who've": "who have", "why's": "why is", 
                      "why've": "why have", "will've": "will have", "won't": "will not", 
                      "won't've": "will not have", "would've": "would have", "wouldn't": "would not", 
                      "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would",
                      "y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",
                      "you'd": "you would", "you'd've": "you would have", "you'll": "you will", 
                      "you'll've": "you will have", "you're": "you are", "you've": "you have", "bharatiya janata party" : "bjp",
                      "inc" : "congress","@narendramodi":"modi", "pappu":"rahul gandhi","gandhi":"rahul gandhi", "@rahulgandhi":"Rahul Gandhi"}
      text = text.lower()
      temp = ""
      for i in text.split():
          if i not in stopw:
              try:
                  temp+=contraction[i]+' '
              except:
                  temp+= i+' '
      text = temp.strip()
      text = re.sub(r'http\S+','', text)
      text = text.lower().translate(remove_punctuation_map)
      text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
      text = re.sub(r"what's", "what is ", text)
      text = re.sub(r"\'s", " ", text)
      text = re.sub(r"\'ve", " have ", text)
      text = re.sub(r"n't", " not ", text)
      text = re.sub(r"i'm", "i am ", text)
      text = re.sub(r"\'re", " are ", text)
      text = re.sub(r"\'d", " would ", text)
      text = re.sub(r"\'ll", " will ", text)
      text = re.sub(r",", " ", text)
      text = re.sub(r"\.", " ", text)
      text = re.sub(r"!", " ! ", text)
      text = re.sub(r"\/", " ", text)
      text = re.sub(r"\^", " ^ ", text)
      text = re.sub(r"\+", " + ", text)
      text = re.sub(r"\-", " - ", text)
      text = re.sub(r"\=", " = ", text)
      text = re.sub(r"'", " ", text)
      text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
      text = re.sub(r":", " : ", text)
      text = re.sub(r" e g ", " eg ", text)
      text = re.sub(r" b g ", " bg ", text)
      text = re.sub(r" u s ", " american ", text)
      text = re.sub(r"\0s", "0", text)
      text = re.sub(r" 9 11 ", "911", text)
      text = re.sub(r"e - mail", "email", text)
      text = re.sub(r"j k", "jk", text)
      text = re.sub(r"\s{2,}", " ", text)
      text = text.replace("bhartiya janata party",'bjp')
      text = text.replace("indian national congress", 'congress')
      text = text.replace("aam aadmi party", 'aap')
      text = text.replace("narendra modi", 'modi')
      text = text.replace("rahulgandhi", 'rahul gandhi')
      temp=''
      for i in text:
          if i.isdigit()==False:
              temp+=i
      text = temp
      text = text.split()
      stemmed_words = [stemmer.stem(word) for word in text]
      text = " ".join(stemmed_words)
      s=""
      for i in text.strip():
        s+=lemmatizer.lemmatize(i)


      return s    


def embed(input):
        return model(input)

def similarity_measure(messages_):
     message_embeddings_=embed(messages_)
     distance1 = scipy.spatial.distance.cdist([message_embeddings_[0]],[message_embeddings_[1]],"cosine")[0]
     return 1-distance1
@app.route("/predict", methods=["POST"])
def predict():
         
         top_k = (flask.request.form["top_k"]).split(",")
        #  print(top_k)
         text=flask.request.form["text"]
         text=clean(text)
         df=pd.read_csv('/symptoms/1.csv')
         y=df['sl.no']
         X=df['Symptoms']
         for i in X:
             if i in top_k:
                 print(1)
        #  print("HERE")
         for i in range(len(X)):
              X[i]=clean(X[i])
         skin_ailments=dict()
         for i in range(len(df)):
              if df['Name'][i] in skin_ailments:
                    skin_ailments[df['Name'][i]].append(df['Symptoms'][i])
              else:
                    skin_ailments[df['Name'][i]]=[df['Symptoms'][i]]
         max1=float('-inf')
         for i in top_k:
            for j in skin_ailments[i]:
                messages =[j,text]
                #print(similarity_measure(messages),i)
                if similarity_measure(messages)>max1:
                    max1=similarity_measure(messages)
                    res=i
         return jsonify(resultant_class=res.upper()), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)