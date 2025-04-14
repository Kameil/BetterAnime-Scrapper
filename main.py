from betteranime import Betteranime

Betteranime = Betteranime()

while True:

    anime = input("Pesquise um anime:")

    animes = Betteranime.search_by_title(anime)

    for anime in animes:
        print(anime.name)
        print(f"Image_url = {anime.image_url}")
        print(anime.episodes_count)
        print(anime.url)
        print("-"*30)