"""
    betteranime.types.Anime"""

from typing import Optional

class Anime:
    """Classe para armazenar informações do anime"""
    def __init__(self, title: str = "", episode: Optional[str] = None, url: Optional[str] = None):
        self.title = title
        self.episode = episode
        self.url = url

    def __repr__(self):
        return f"<Anime title='{self.title}', episode='{self.episode}', url='{self.url}'>"
