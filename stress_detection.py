import pandas as pd
import numpy as np
import nltk
import re
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB


def isthisstress(da_tweet):


    def clean(text):
        text = str(text).lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text = [word for word in text.split(' ') if word not in stopword]
        text = " ".join(text)
        text = [stemmer.stem(word) for word in text.split(' ')]
        text = " ".join(text)
        return text


    nltk.download('stopwords')
    stemmer = nltk.SnowballStemmer("english")

    stopword = set(stopwords.words('english'))
    data = pd.read_csv("stress.csv")
    data["text"] = data["text"].apply(clean)

    data["label"] = data["label"].map({0: "No Stress", 1: "Stress"})
    data = data[["text", "label"]]

    x = np.array(data["text"])
    y = np.array(data["label"])


    cv = CountVectorizer()
    X = cv.fit_transform(x)
    xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.33, random_state=42)

    model = BernoulliNB()
    model.fit(xtrain, ytrain)

    #user = input("Enter your tweet: ")
    data = cv.transform([da_tweet]).toarray()
    output = model.predict(data)
    return output
