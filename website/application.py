from flask import Flask, render_template, url_for, redirect, request
from models.player import Player
from models.song_library import SongLibrary 
from models.database import DataBase

app = Flask(__name__)
music_player = Player()
song_library = SongLibrary()
db = DataBase()
db.create_playlist("chill","HAPPY")
playlists = db.get_all_playlists()

@app.route('/')
def home():
	return render_template("index.html", **{"show_songs": True, "songs": playlists[0].songs})

@app.route("/play/")
def play():
	if music_player.is_playing():
		pause()
	else:
		play_song("song")

	return redirect(url_for("home"))

def play_song(song):
	try:
		sng = song_library.search(song)[0]
		music_player.play(sng)
	except:
		print("[LOG] Please start the music server")

def pause():
	try:
		music_player.pause()
	except:
		print("[LOG] Pleas start the music server")

if __name__ == "__main__":
	app.run(debug = True)