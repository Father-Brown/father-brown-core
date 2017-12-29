import urllib.request
from bs4 import BeautifulSoup
from database.DataBase import DataBase


class ScrapySempreQuestione():

    def __init__(self,site_name, url_noticia):
        response = urllib.request.urlopen(url_noticia)
        self.soap = BeautifulSoup(response, 'html.parser')
        self.site_name=site_name

    def process(self):
        [s.extract() for s in self.soap('script')]# removendo qualquer tag scrip no corpo da noticia
        [s.extract() for s in self.soap.find_all(text='Veja o Vídeo Abaixo:')]  # removendo
        [s.decompose() for s in self.soap.find_all('div',text='Veja também:')]  # removendo
        self.title = self.soap.find_all(class_="post-title entry-title")[0].get_text()
        elements=self.soap.find_all(class_="post-body entry-content")
        # print(self.title)
        base = DataBase()
        for content in elements:
            value = content.get_text()
            value = value.replace('\n', '')
            base.save_news(self.site_name, self.title, value, 'FALSE')
            print(value)