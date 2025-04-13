from betteranime import Betteranime

Betteranime = Betteranime()

releases = Betteranime.get_lastest_releases()

for anime in releases:
    print(f"Title: {anime.title}")
    print(f"Episode: {anime.episode}")
    print(f"URL: {anime.url}")
    print("-" * 20)