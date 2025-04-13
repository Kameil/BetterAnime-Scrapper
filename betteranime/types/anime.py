"""
    betteranime.types.Anime"""

from typing import Optional

class LatestAnime:
    def __init__(self, title: str = "", episode: Optional[str] = None, url: Optional[str] = None):
        """Classe para armazenar informações do anime"""
        self.title = title
        self.episode = episode
        self.url = url

    def __repr__(self):
        return f"<Anime title='{self.title}', episode='{self.episode}', url='{self.url}'>"
