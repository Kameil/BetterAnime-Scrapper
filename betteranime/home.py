"""
Todos os comanndos para a pagina inicial do betteranime.net
"""

from typing import Optional, List
import requests
from bs4 import BeautifulSoup
from betteranime.types import LatestAnime

class Home:
    def __init__(self, url: str, session: requests.Session):
        """ Pagina Inicial do Betteranime"""
        self.url = url
        self.session = session
         

    def get_lastest_releases(self) -> Optional[List[LatestAnime]]:
        """
        Pegar Lista dos ultimos animes lancados.
        
        exemplo:
        ```python
        from betteranime import Betteranime

        Betteranime = Betteranime()

        releases = Betteranime.get_lastest_releases()

        for anime in releases:
            print(f"Title: {anime.title}")
            print(f"Episode: {anime.episode}")
            print(f"URL: {anime.url}")
            print("-" * 20)
        ```
        """
        response = self.session.get(self.url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        animes: List[LatestAnime] = []

        articles = soup.find_all("article")
        for article in articles:
            informacoes = article.find("div", class_="card-title")
            if informacoes:
                title = informacoes.find("h3")
                episode = informacoes.find("h4")
                if title and episode:
                    title = title.text.strip()
                    episode = episode.text.strip().split(" ")[1]
                    anime = LatestAnime(title, episode)
                    animes.append(anime)
        return animes
        


