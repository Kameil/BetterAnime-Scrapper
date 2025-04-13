"""
Todos os comanndos para a pagina inicial do betteranime.net
"""

from typing import Optional, List
import requests
from bs4 import BeautifulSoup


class Anime:
        """ Classe para armazenar informacoes do anime"""
        def __init__(self, title = "", episode: Optional[str] = None, url: Optional[str] = None):
            self.title: str = title
            self.episode: Optional[str] = episode
            self.url: Optional[str] = url

class Home:
    def __init__(self, url: str):
        """ Pagina Inicial do Betteranime"""
        self.url = url
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"}
         

    def get_lastest_releases(self) -> Optional[List[Anime]]:
        """Pegar Lista dos ultimos animes lancados."""
        response = requests.get(self.url, headers=self.headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        animes: List[Anime] = []

        articles = soup.find_all("article")
        for article in articles:
            informacoes = article.find("div", class_="card-title")
            if informacoes:
                title = informacoes.find("h3")
                episode = informacoes.find("h4")
                if title and episode:
                    title = title.text.strip()
                    episode = episode.text.strip().split(" ")[1]
                    print(f"Title: {title}, Episode: {episode}")
                    anime = Anime(title, episode)
                    animes.append(anime)
        return animes
        


