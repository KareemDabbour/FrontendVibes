import time
from .song import Song

class Playlist:
	def __init__(self, name, vibe=None):
		self.name = name
		self.date_created = time.time()
		self.vibe = vibe
		self.songs = []
		self.id = None

	def set_id(self, _id):
		self.id = str(_id)
		
	def change_name(self, name):
		self.name = name

	def change_vibe(self, vibe):
		self.vibe = vibe

	def add_song(self, song):
		"""
		add a given song object to the playlist
		:param song: Song
		"""
		if isinstance(song, Song):
			self.songs.append(song)
		else:
			raise Exception("Argument must be a Song object")

	def remove_song(self, song):
		if song in self.songs:
			song.remove(song)
		else:
			raise Exception("No such song")

	def __repr__(self):
		return f"Playlist(Name: {self.name}, Vibe: {self.vibe}, # Songs {len(self.songs)}, String: {self.id})"
