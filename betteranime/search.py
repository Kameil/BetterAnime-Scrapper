"""
classe responsavel pela pesquisa. a unica classe necessaria 
"""


from functools import lru_cache
import requests
from typing import List, Optional
from bs4 import BeautifulSoup

from betteranime.types import SearchedAnime

class Pesquisa:
    def __init__(self, url:str, session: requests.Session):
        """
        Aqui ficaremos com as funcoes de pesquisa
        """
        self.url = url + "/pesquisa?titulo="
        self.session = session

    @lru_cache(maxsize=128)
    def search_by_title(self, title: str) -> Optional[List[SearchedAnime]]:
        """
        pesquisa por titulo de anime
        """

        response = self.session.get(self.url + title)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        animes: List[SearchedAnime] = []

        articles = soup.find_all("article")

        for article in articles:
            anime_url = self._get_anime_url(article)
            anime_image_url = self._get_anime_image_url(article)
            episodes_count = self._get_anime_episodes_count(article)
            anime_title = self._get_anime_title(article, anime_url)

            animes.append(SearchedAnime(
                name=anime_title,
                url=anime_url,
                image_url=anime_image_url,
                episodes_count=episodes_count
            ))

        return animes
    
    def _get_anime_url(self, article: BeautifulSoup) -> str:
        a = article.find("a")
        if a.has_attr("href"):
            anime_url = a["href"]
            return anime_url
        raise ValueError("Nao foi possivel Obter a url do anime.")
    
    def _get_anime_image_url(self, article: BeautifulSoup) -> Optional[str]:
        div = article.find("div", class_="card-vertical-img")
        image = div.find("img")
        if image and image.has_attr("src"):
            return "https:" + image["src"]
        return None
    
    def _get_anime_title(self, article: BeautifulSoup, url:str) -> str:
        a = article.find("a")
        if a.has_attr("title"):
            anime_url = a["title"]
            return anime_url
        return url.split("/")[-1].replace("-", " ")
    
    def _get_anime_episodes_count(self, article: BeautifulSoup) -> Optional[int]:
        div = article.find("div", class_="card-vertical-episodes")
        episodes = div.find("span")
        if episodes:
            try:
                return int(''.join(filter(str.isdigit, episodes.text)))
            except ValueError:
                return None
        return None

        