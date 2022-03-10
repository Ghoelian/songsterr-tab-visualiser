import requests
import urllib

class API:
    def getSongs(self, query):
        query = urllib.parse.quote_plus(query)
        response = requests.get(
            f"https://www.songsterr.com/a/ra/songs.json?pattern={query}&inst=drums")

        return response.json()
