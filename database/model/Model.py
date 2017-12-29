from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

class News(StructuredNode):
    title = StringProperty(unique_index=True)
    content = StringProperty(unique_index=True)
    site = RelationshipTo('Site', 'PUBLICOU')
    tipo = RelationshipFrom('Tipo', 'E')


class Site(StructuredNode):
    name = StringProperty(unique_index=True)
    news = RelationshipFrom('News', 'PUBLICOU')

class Tipo(StructuredNode):
    description = StringProperty(unique_index=True)
    news = RelationshipFrom('News', 'E')