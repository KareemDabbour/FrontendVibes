from flask import Flask, render_template, url_for, redirect, request
from models.player import Player
from models.song_library import SongLibrary 
from models.database import DataBase
from models.song import Song
import random

app = Flask(__name__)

music_player = Player()
song_library = SongLibrary()
VIBES = ["HAPPY", "SAD", "ENERGETIC", "CALM"]


@app.route("/playlist/<_id>")
def songs(_id):
	db = DataBase()

	x = db.get_playlists_by_id(int(_id))
	rep = {"show_playlists": x != None, "playlist": x}
	return render_template("index.html", **rep)


@app.route("/")
def home():
	query = request.args.get("search")
	play = request.args.get("play")
	fast_forward = request.args.get("ff")
	rewind = request.args.get("rewind")
	ref = {}
	if play:
		play_queue()
	elif fast_forward:
		music_player.pop_song()
		play_queue()
	elif rewind:
		if len(music_player.song_queue) > 0: 
			play_song(music_player.song_queue[0])
	elif query:
		results = song_library.search(query)
		ref = {"results":results, "search":query}
	
	return render_template("index.html", **ref)
	

@app.route("/list/<vibe>")
def playlists(vibe):
	db = DataBase()
	if vibe in VIBES:
		rep = {"show_playlists": True, "playlists": db.get_playlists_by_vibe(vibe)}
		return render_template("index.html", **rep)

	return redirect(url_for("home"))


def play_queue():
	if music_player.is_playing():
		pause()
	else:
		try:
			music_player.resume()
		except: 
			if len(music_player.song_queue) > 0:
				play_song(music_player.song_queue[0])

	return redirect(url_for("home"))

def play_song(song):
	music_player.play(song)


def pause():
	try:
		music_player.pause()
	except:
		print("[LOG] Pleas start the music server")

if __name__ == "__main__":
	app.run(debug = True)