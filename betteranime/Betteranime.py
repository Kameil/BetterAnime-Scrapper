"""
Classe principal do better anime 
"""


from betteranime import home

class Betteranime:
    def __init__(self, url: str="https://betteranime.net"):
        self.home = home.Home(url)
        self.get_lastest_releases = self.home.get_lastest_releases