import nltk
from database.DataBase import DataBase
from sklearn.model_selection import train_test_split

from facebookapi.publushFacebook import PublishFacebook
from preprocess.Process import Process
from util.Character import removerAcentosECaracteresEspeciais
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

db = DataBase()

data=db.get_all_data_set(['vaticannews', 'semprequestione', 'acidigital', 'cancaonova'])

y = [clazz for (title, news, clazz) in data]
X = [news for (title, news, clazz) in data]




def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    classifier.fit(X_train, y_train)
    print("Accuracy: %s" % classifier.score(X_test, y_test))
    return classifier


import string
from nltk import word_tokenize


def stemming_tokenizer(text):
    stemmer = nltk.stem.RSLPStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]


trial5 = Pipeline([
    ('vectorizer', TfidfVectorizer(tokenizer=stemming_tokenizer,
                                   stop_words=stopwords.words('portuguese') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.05)),
])


c=train(trial5, X, y)
data2 =db.get_all_news_from_no_class('semprequestione')
n=list()
for (title, news, clazz) in data2:
    n.append(news)

result=c.predict(n)

for i in range(len(data2)):
    titulo, news, clazz= data2[i]
    # print(titulo)
    # print(result[i])
    if "Papa João XIII conheceu e conversou 20 minutos com um extraterrestre pessoalmente anos antes de morrer" in titulo:
        news =db.get_news_by_title(titulo)
        if result[i] == 'False':
            pb = PublishFacebook()
            pb.publish("Fake news detectada, Você pode me ajudar a verificar?  \n"+news.url)