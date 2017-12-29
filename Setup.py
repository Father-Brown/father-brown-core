
from preprocess.scrapy.ScrapySempreQuestione import ScrapySempreQuestione
from util.general import file_to_set

sites = set()
sites = file_to_set('crawled.txt')
for url in sites:
    t = ScrapySempreQuestione('http://www.semprequestione.com/', url)
    t.process()

# from neomodel import config
# from database.model.Model import News
# from database.model.Model import Site
# from database.model.Model import Tipo
# # from father.brown.database.model.Site import Site
#
#
#
# config.DATABASE_URL = 'bolt://neo4j:st1215@localhost:7687'
#
#
#
# site = Site(name='http://www.semprequestione.com/').save()
#
# news = News()
# news.title="Vaticano: Bento XVI diz que cardeal Müller «defendeu a tradição» no espírito do Papa Francisco"
# news.content="da Fé saiu do cargo em 2017 Cidade do Vaticano, 27 dez 2017 (Ecclesia) – O Papa emérito Bento XVI agradeceu ao cardeal alemão Gerhard Ludwig Müller pelo seu trabalho como prefeito da Congregação para a Doutrina da Fé, concluído em 2017.“[O cardeal Müller] Defendeu as claras tradições da fé, mas no espírito do Papa Francisco procurou entender como podem ser vividas hoje”, refere Bento XVI, numa saudação que abre o livro ‘O Deus Trino. Fé cristã na era secular’.O volume (editado por Herder) foi publicado em alemão por ocasião do 70.º aniversário de D. Gerhard Ludwig Müller (31 de dezembro de 2017) e do seu 40º aniversário de sua ordenação sacerdotal.“Um sacerdote - e certamente um bispo e um cardeal - nunca simplesmente se aposenta”, realça o Papa emérito.Na obra, de quase 700 páginas, há, entre outros, as contribuições dos cardeais Reinhard Marx, Angelo Scola e Kurt Koch, dos arcebispos Rino Fisichella e Bruno Forte, e do sucessor do cardeal Müller, D. Luis Ladaria, informa o portal de notícias do Vaticano.Bento XVI recorda que foi Paulo VI quem desejou que um alto cargo no Vaticano fosse designado apenas por cinco anos, a justificação usada pelo Papa Francisco para nomear um novo prefeito da Congregação para a Doutrina da Fé."
# news.save()
#
# news.site.connect(site)
#
# tipo = Tipo(description='TRUE').save()
# news.tipo.connect(tipo)
#
#
# news = News()
# news.title="Vaticano: Bento XVI diz que cardeal Müller «defendeu a tradição» no espírito do Papa Francisco"
# news.content="da Fé saiu do cargo em 2017 Cidade do Vaticano, 27 dez 2017 (Ecclesia) – O Papa emérito Bento XVI agradeceu ao cardeal alemão Gerhard Ludwig Müller pelo seu trabalho como prefeito da Congregação para a Doutrina da Fé, concluído em 2017.“[O cardeal Müller] Defendeu as claras tradições da fé, mas no espírito do Papa Francisco procurou entender como podem ser vividas hoje”, refere Bento XVI, numa saudação que abre o livro ‘O Deus Trino. Fé cristã na era secular’.O volume (editado por Herder) foi publicado em alemão por ocasião do 70.º aniversário de D. Gerhard Ludwig Müller (31 de dezembro de 2017) e do seu 40º aniversário de sua ordenação sacerdotal.“Um sacerdote - e certamente um bispo e um cardeal - nunca simplesmente se aposenta”, realça o Papa emérito.Na obra, de quase 700 páginas, há, entre outros, as contribuições dos cardeais Reinhard Marx, Angelo Scola e Kurt Koch, dos arcebispos Rino Fisichella e Bruno Forte, e do sucessor do cardeal Müller, D. Luis Ladaria, informa o portal de notícias do Vaticano.Bento XVI recorda que foi Paulo VI quem desejou que um alto cargo no Vaticano fosse designado apenas por cinco anos, a justificação usada pelo Papa Francisco para nomear um novo prefeito da Congregação para a Doutrina da Fé."
# news.save()
# # site = Site.nodes.get(name="http://www.agencia.ecclesia.pt")# obter um no pelo nome
# news.site.connect(site)
#
# tipo = Tipo(description='FALSE').save()
# news.tipo.connect(tipo)
