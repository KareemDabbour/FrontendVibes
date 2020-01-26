import sqlite3
from sqlite3 import Error
import os
cwd = os.getcwd()

FILE = "/database/playlists.db" 

class DataBase:
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
		query = """CREATE TABLE Playlists 
					(name text, created date, id int PRIMARY KEY)"""
		
		return self.query

	def execute(self, string):
		self.cursor.execute(string)
		self.cursor.commit()

	def get_all_playlists(self):
		"""
		returns all playlists
		"""
		

	def get_playlist(self, name="", _id=""):
		if not name and not _id:
			raise Exception("Must pass a name or ID")

	def create_playlist(self, playlist):
		pass

  
