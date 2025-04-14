"""
    betteranime.types.Anime
"""

from typing import Optional

class LatestAnime:
    def __init__(self, title: str = "", episode: Optional[str] = None, url: Optional[str] = None):
        """Classe para armazenar informações do anime"""
        self.title = title
        self.episode = episode
        self.url = url

    def __repr__(self):
        return f"<Anime title='{self.title}', episode='{self.episode}', url='{self.url}'>"
    

class SearchedAnime:
    def __init__(self, name: str, episodes_count: str, url: str, image_url: str):
        """ Classe para armazenar informacoes de animes pesquisados tendeu"""
        self.name = name
        self.episodes_count = episodes_count
        self.url = url
        self.image_url = image_url

    def __repr__(self):
        return f"<SearchedAnime name='{self.name}', episodes='{self.episodes_count}', url='{self.url}'>"
