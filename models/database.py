import sqlite3
from sqlite3 import Error
import os
import time
import pickle
cwd = os.getcwd()

FILE = "/database/playlists.db" 
PLAYLIST_TABLE = "Playlists"

class DataBase:
	pass
	'''
	def __init__(self):
		self.liked_songs = None
		self.playlists = None

		conn = None
	    try:
	        conn = sqlite3.connect(FILE)
	        print(sqlite3.version)
	    except Error as e:
	        print(e)
	    finally:
	        if conn:
	            conn.close()

	    self.cursor = conn.cursor()

	def _create_table(self):
		query = f"""CREATE TABLE {PLAYLIST_TABLE}
					(name text, created date, songs BLOB,id int PRIMARY KEY AUTOINCREMENT)"""
		self.cursor.execute(query)
		self.cursor.commit()

	def get_all_playlists(self):
		"""
		returns all playlists
		"""
		query = f"SELECT * FROM {PLAYLIST_TABLE}"
		self.cursor.execute(query)
		result = self.cursor.fetchall()
		for r in result:
			print(r)

	def get_playlist(self, name="", _id=""):
		"""
		returns a new playlist object
		"""
		if not name and not _id:
			raise Exception("Must pass a name or ID")

		query = f"SELECT * FROM {PLAYLIST_TABLE} WHERE NAME = {name} "

	def create_playlist(self, name):
		"""
		returns: Playlist object
		"""
		pl = Playlist(name)
		query = f"INSERT INTO {PLAYLIST_TABLE} VALUES (?, ?)\
				({name}, {time.time()})"
		self.cursor.execute(query)
		self.cursor.commit()
		last_row = 

	def update_playlist(self, _id):
  		pass
'''