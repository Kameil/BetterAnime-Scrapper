"""
Classe principal do better anime 
"""


from betteranime import home
from betteranime import search
import requests
from typing import Dict

class Betteranime:
    def __init__(self, url: str="https://betteranime.net",
                headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"}):
        session = requests.Session()
        session.headers.update(headers)
        self.session = session

        # home
        self.home = home.Home(url, self.session)
        self.get_lastest_releases = self.home.get_lastest_releases

        # search
        self.search = search.Pesquisa(url, self.session)
        self.search_by_title = self.search.search_by_title