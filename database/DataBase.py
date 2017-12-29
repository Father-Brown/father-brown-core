from neomodel import config
from database.model.Model import News
from database.model.Model import Site
from database.model.Model import Tipo
# from father.brown.database.model.Site import Site

class DataBase:

    def __init__(self):
        config.DATABASE_URL = 'bolt://neo4j:st1215@localhost:7687'

    def save_news(self, siteName, title, content, clazz):
        site = Site.nodes.get(name=siteName)
        news = News()
        news.title=title
        news.content=content
        news.save()
        news.site.connect(site)
        tipo = Tipo(description=clazz).save()
        news.tipo.connect(tipo)