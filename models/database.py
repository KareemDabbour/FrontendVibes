import sqlite3

class DataBase:
	def __init__(self):
		self.liked_songs = None
		self.playlists = None

	def get_all_playlists(self):
		"""
		returns all playlists
		"""
		pass

	def get_playlist(self, name="", _id=""):
		if not name and not _id:
			raise Exception("Must pass a name or ID")

	def create_playlist(self, playlist):
		pass


