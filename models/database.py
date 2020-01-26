import sqlite3
from sqlite3 import Error
import os
from datetime import datetime
import pickle
from playlist import Playlist

cwd = os.getcwd()

FILE = "playlists.db" 
PLAYLIST_TABLE = "Playlists"
VIBES = ["HAPPY", "CALM", "SAD", "ENERGETIC"]

class DataBase:
    def __init__(self):
        self.liked_songs = None
        self.playlists = None

        self.conn = None
        try:
            self.conn = sqlite3.connect(FILE)
        except Error as e:
            print(e)

        self.cursor = self.conn.cursor()
        self._create_table()

    def close(self):
        self.conn.close()

    def _create_table(self):
        query = f"""CREATE TABLE IF NOT EXISTS {PLAYLIST_TABLE}
                    (name TEXT, created date, vibe TEXT,songs BLOB,id INTEGER PRIMARY KEY AUTOINCREMENT)"""
        self.cursor.execute(query)
        self.conn.commit()

    def get_all_playlists(self):
        """
        returns all playlists
        """
        query = f"SELECT * FROM {PLAYLIST_TABLE}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        results = []
        for r in result:
            name, date, vibe, songs, _id = r
            pl = Playlist(name, vibe)
            pl.date = date
            pl.songs = pickle.loads(songs)
            pl.id = _id
            results.append(pl)

        return results

    def get_playlists_by_vibe(self, vibe):
        vibe = vibe.upper()
        query = f"SELECT * FROM {PLAYLIST_TABLE} WHERE vibe =?"
        self.cursor.execute(query, (vibe,))

        result = self.cursor.fetchall()

        results = []
        for r in result:
            name, date, vibe, songs, _id = r
            pl = Playlist(name, vibe)
            pl.date = date
            pl.songs = pickle.loads(songs)
            pl.id = _id
            results.append(pl)

        return results

    def get_playlists_by_id(self, _id):
        vibe = vibe.upper()
        query = f"SELECT * FROM {PLAYLIST_TABLE} WHERE id = {_id}"
        self.cursor.execute(query)

        result = self.cursor.fetchone()

        name, date, vibe, songs, _id = result
        pl = Playlist(name, vibe)
        pl.date = date
        pl.songs = pickle.loads(songs)
        pl.id = _id

        return result

    def create_playlist(self, name, vibe):
        """
        returns: Playlist object
        """
        vibe = vibe.upper()
        if not name or vibe not in VIBES:
            raise Exception(f"Invalid arguments, name cannot be null and name must be in {VIBES}")

        pl = Playlist(name)
        query = f"INSERT INTO {PLAYLIST_TABLE} VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (name, datetime.now(),vibe,pickle.dumps([]), None))
        self.conn.commit()
        self.cursor.execute("SELECT last_insert_rowid()")
        row = self.cursor.fetchone()
        pl.set_id(row[0]) 

    def update_playlist(self, _id, playlist):
        query = f"UPDATE {PLAYLIST_TABLE} set songs={pickle.dumps(playlist.songs)} WHERE id = {_id}"
        self.cursor.execute(query)
        self.conn.commit


if __name__ == "__main__":
    db = DataBase()
    ls = db.get_playlists_by_vibe("HAPPY")
    print(ls)