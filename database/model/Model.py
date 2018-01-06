from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo


class Tipo(GraphObject):
    __primarykey__ = "description"
    description = Property()
    news = RelatedFrom('News', 'E')

class News(GraphObject):
    __primarykey__ = "title"
    title = Property()
    sub_title = Property()
    url = Property()
    site= RelatedFrom('Site', 'PUBLICOU')
    tipo = RelatedTo(Tipo, 'E')
    content = Property()



class Site(GraphObject):
    __primarykey__ = "name"
    name = Property()
    url = Property()
    news = RelatedTo(News)


