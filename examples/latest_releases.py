from ..betteranime import Betteranime
from ..betteranime.types import LatestAnime

Betteranime = Betteranime()

releases = Betteranime.get_lastest_releases()

for anime in releases[::-1]:
    print(f"Title: {anime.title}")
    print(f"Episode: {anime.episode}")
    print(f"URL: {anime.url}")
    print("-" * 20)

