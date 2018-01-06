import nltk


class Process:
    def __init__(self, dataSet):
        self.stopWords = nltk.corpus.stopwords.words('portuguese')
        self.dataSet=dataSet


    def stemmerAplay(self ):
        """
        Extrai o radical das palavras
        :param dataSet:
        :return:
        """
        stemmer = nltk.stem.RSLPStemmer()
        text = []
        for (news, clazz) in self.dataSet:
            comstemmer =[str(stemmer.stem(p)) for p in news.split() if p not in self.stopWords]
            text.append((comstemmer, clazz))
        return text

    def buscaPalavras(self):
        """
        Busca todas as palavras que existem na base de dados
        :param dataSet:
        :return:
        """
        dataSet=self.stemmerAplay()
        todasPalavras =[]
        for (notice, clazz) in dataSet:
            todasPalavras.extend(notice)
        return todasPalavras

    def freqWords(self, words):
        """
        Calcula a frequencia das palavras
        :param words:
        :return:
        """
        return nltk.FreqDist(words)

    def unicWords(self):
        """
        Busca as palavras unicas
        :param words:
        :return:
        """
        words=self.buscaPalavras()
        return self.freqWords(words).keys()

    def extrairFrase(self, documento):
        """
        Mostra de uma frase contem ou nao na base de dados (documento)
        :param documento:
        :return:
        """
        unicWords = self.unicWords()
        doc = set(documento)
        caracteristicas ={}
        for palavras in unicWords:
            caracteristicas['%s'%palavras]=(palavras in doc)
        return caracteristicas


    def classify(self, dataSet):
        """
        Recebe um dataSet e aplica o extrairFrase para o dataSet
        :param dataSet:
        :return:
        """

        return nltk.classify.apply_features(self.extrairFrase, dataSet)


from database.DataBase import DataBase


db = DataBase()

dataSet=db.get_all_data_set(['vaticannews', 'semprequestione'])

# data=db.get_all_news_from('vaticannews')

p = Process(dataSet)
sp =p.stemmerAplay()
# print(p.extrairFrase())
print(type(p.extrairFrase(dataSet)))
print(type(p.freqWords(p.buscaPalavras()).values()))

# d=p.freqWords(p.buscaPalavras()).
# classificador=nltk.NaiveBayesClassifier.train(d)
# #
# print(classificador.show_most_informative_features(10))
# for s in st.most_common(50):
#     print(s)

