"""
Classe principal do better anime 
"""


from betteranime import home

class Betteranime:
    def __init__(self, url: str="https://betteranime.net"):
        self.Home = home.Home(url)
        self.get_lastest_releases = self.Home.get_lastest_releases