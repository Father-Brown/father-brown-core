import nltk

from database.DataBase import DataBase
from preprocess.Process import Process
from util.Character import removerAcentosECaracteresEspeciais

def stimmer(text):
    text=removerAcentosECaracteresEspeciais(text)
    testestemming = []
    stemmer = nltk.stem.RSLPStemmer()
    for palavrastreinamento in text.split():
        comstem = [p for p in palavrastreinamento.split()]
        testestemming.append(str(stemmer.stem(comstem[0])))
        # print(testestemming)

    novo = p.extrairFrase(testestemming)
    print(text)
    print('É '+classificador.classify(novo))

    distribuicao = classificador.prob_classify(novo)
    for classe in distribuicao.samples():
        print("%s: %f" % (classe, distribuicao.prob(classe)))

db = DataBase()
# db.delete()




data=db.get_all_data_set(['vaticannews', 'semprequestione', 'acidigital', 'cancaonova'])

p=Process(data)
frases=p.stemmerAplay()
basecompleta=p.classify(frases)
classificador=nltk.NaiveBayesClassifier.train(basecompleta)
#
# print(classificador.show_most_informative_features(10))

# teste ="funcionários do Vaticano e com suas amantes e deu este conselho aos pais: “Sempre briguem diante das crianças. Nunca! Em uma audiência realizada na quinta-feira, 21 de dezembro, com os funcionários da Santa Sé para desejar-lhes Feliz Natal, o Santo Padre fez uma série de reflexões sobre a família.Francisco mostrou a sua preocupação pelas crises conjugais que afetam algumas famílias."

# teste='O Papa Francisco lançou duras críticas aos media que espalham e se concentram em escândalos e notícias falsas, afirmando que correm o risco de se tornarem pessoas que possuem o fascínio mórbido por… excrementos.PUBEm entrevista ao semanário católico belga Tertio, e citado pela Reuters, Francisco realçou que espalhar a desinformação é “provavelmente o maior estrago que os media podem fazer”, garantindo que este tipo de actividade em vez de educar o público é um pecado.Utilizando uma terminologia curiosa e pouco comum, o Papa afirmou que a comunicação social deve evitar a “coprofilia” – nome dado a um invulgar interesse e excitação provocada por fezes. E, segundo o líder da Igreja Católica, aqueles que consomem histórias falsas correm o risco de se tornarem coprofágicos. Isto é, pessoas que ingerem fezes.'

data2 =db.get_all_news_from_no_class('acidigital')
for d in data2:
    stimmer(d)
#     teste,clazz=d
#     testestemming = []
#     stemmer = nltk.stem.RSLPStemmer()
#     for palavrastreinamento in teste.split():
#         comstem = [p for p in palavrastreinamento.split()]
#         testestemming.append(str(stemmer.stem(comstem[0])))
#         # print(testestemming)
#
#
#     novo = p.extrairFrase(testestemming)
#
#     # print(novo)
#     # print(classificador.labels())
#     print(d)
#     print('É '+classificador.classify(novo))
#
#     distribuicao = classificador.prob_classify(novo)
#     for classe in distribuicao.samples():
#         print("%s: %f" % (classe, distribuicao.prob(classe)))




# teste='Francisco convida a imitar a Virgem Maria, por uma Igreja “pobre de coisas e rica de amor” Da redação, com Agência Ecclesia  Na Missa da Solenidade de Santa Maria Mãe de Deus, nesta segunda-feira, 1º, o Papa Francisco fez um apelo à defesa da vida. “A humanidade é querida e sagrada para o Senhor. Por isso, servir a vida humana é servir a Deus, e toda a vida – desde a vida no ventre da mãe, até à vida envelhecida, atribulada e doente, à vida incômoda e até repugnante – deve ser acolhida, amada e ajudada”, disse o Santo Padre na Basílica de São Pedro. O Pontífice fez uma intervenção centrada na figura da “Mãe de Deus”, a solenidade que marca o início do ano, no calendário litúrgico católico. “Maria é exatamente como Deus nos quer, como quer a sua Igreja: Mãe terna, humilde, pobre de coisas e rica de amor, livre do pecado, unida a Jesus, que guarda Deus no coração e o próximo na vida”, sublinhou. Imitar a Virgem Maria uma alusão ao novo ano civil, Francisco convidou os católicos a imitar a Virgem Maria. “Para avançar – diz-nos a festa de hoje –, é preciso recuar: recomeçar do presépio, da Mãe que tem Deus nos braços”, precisou. O Papa realçou em particular a necessidade do silêncio, onde Deus se revela a cada pessoa, convidando os fiéis a dedicar um momento à oração silenciosa, no seu dia, diante do presépio. “Reservar cada dia um tempo de silêncio com Deus é guardar a nossa alma; é guardar a nossa liberdade das banalidades corrosivas do consumo e dos aturdimentos da publicidade, da difusão de palavras vazias e das ondas avassaladoras das maledicências e da balbúrdia”, observou. Maternidade e segredos de Maria  homilia chamou a atenção para a dimensão de maternidade que é valorizada na solenidade de hoje. “Eis o milagre, a novidade: o homem já não está sozinho; nunca mais será órfão, é para sempre filho. O Ano tem início com esta novidade. E nós proclamamo-la dizendo assim: Mãe de Deus! É a alegria de saber que a nossa solidão está vencida”, referiu o Pontífice. “Dizer «Mãe de Deus» lembra-nos isto: Deus está perto da humanidade como uma criança da mãe que a traz no ventre”, acrescentou.  Papa apresentou ainda os “segredos” da Virgem Maria como forma de viver melhor o novo ano: “guardar no silêncio e levar a Deus”. “Também nós – cristãos em caminho –, no começo do ano, sentimos a necessidade de recomeçar do centro, deixar para trás os pesos do passado e partir do que é importante. Temos hoje diante de nós o ponto de partida: a Mãe de Deus”, declarou. Devoção à Maria rancisco considerou que a devoção à Maria é “uma exigência da vida cristã”, que permite deixar de lado “tantas bagatelas inúteis” e reencontrar “aquilo que conta”. “Para que a fé não se reduza apenas a ideia ou doutrina, precisamos, todos, de um coração de mãe que saiba guardar a ternura de Deus e ouvir as palpitações do homem”, prosseguiu. No final da homilia, o Papa convidou a assembleia a repetir, três vezes, com ele: “Santa Mãe de Deus”. Cumprindo a tradição, um grupo de três crianças liderou a procissão da apresentação dos dons, vestidos de Reis Magos, em representação dos ‘sternsinger’ (cantores da estrela) que na Alemanha, Áustria e Suíça passam pelas casas para anunciar o nascimento do Senhor e recolher ofertas para as crianças necessitadas.'
# stimmer(teste)