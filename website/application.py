from flask import Flask, render_template, url_for, redirect, request
from models.player import Player
from models.song_library import SongLibrary 
from models.database import DataBase
from models.song import Song

app = Flask(__name__)

music_player = Player()
song_library = SongLibrary()
VIBES = ["HAPPY", "SAD", "ENERGETIC", "CALM"]

@app.route("/")
def home(data=None):
	return render_template("index.html")
		
@app.route("/list/<vibe>")
def playlists(vibe):
	db = DataBase()
	if vibe in VIBES:
		rep = {"show_playlists": True, "playlists": db.get_playlists_by_vibe(vibe)}
		return render_template("index.html", **rep)

	return redirect(url_for("home"))

@app.route("/playlist/<_id>")
def songs(_id):
	db = DataBase()
	ids = filter(lambda x: x.id, db.get_all_playlists())

	if _id in ids:
		rep = {"show_playlists": True, "playlists": db.get_playlists_by_id(_id)}
		return render_template("index.html", **rep)

	return redirect(url_for("home"))

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