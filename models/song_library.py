import requests
from .song import Song

class SongLibrary:
	QUERY_URL = "https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs?query="
	SONG_ID = "https://conuhacks-2020.tsp.cld.touchtunes.com/v1/songs/"
	HEADERS = {"Authorization": "mws96s3um14n8gqu0vmm4rapx3uhoz6l"}

	def search(self, song="", artist="", results=10):
		url = self.QUERY_URL + song.replace(" ", "*")

		payload = {}
		headers = {
		  'Authorization': 'mws96s3um14n8gqu0vmm4rapx3uhoz6l'
		}

		response = requests.request("GET", url, headers=headers, data = payload).json()

		results = []
		for r in response["songs"]:
			song = Song(r["title"], r["id"], r["artistName"], r["duration"], r["genreName"])
			results.append(song)

		return results

	def search_by_id():
		url = self.SONG_ID + song.replace(" ", "*")

		payload = {}
		headers = {
		  'Authorization': 'mws96s3um14n8gqu0vmm4rapx3uhoz6l'
		}

		response = requests.request("GET", url, headers=headers, data = payload).json()

		r = response
		
		song = Song(r["title"], r["id"], r["artistName"], r["duration"], r["genreName"])

		return song

		