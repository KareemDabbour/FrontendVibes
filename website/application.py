from flask import Flask, render_template, url_for, redirect, request, session
from models.player import Player
from models.song_library import SongLibrary 
from models.database import DataBase
from models.song import Song
import random

app = Flask(__name__)
app.secret_key = "hello"

music_player = Player()
song_library = SongLibrary()
db = DataBase()
'''
pl = db.get_playlists_by_id(1)
music_player.add_song(pl.songs[0])
music_player.add_song(pl.songs[1])
pl = db.get_playlists_by_id(1)
music_player.add_song(pl.songs[0])
music_player.add_song(pl.songs[1])'''


VIBES = ["HAPPY", "SAD", "ENERGETIC", "CALM"]


@app.route("/playlist/<_id>")
def songs(_id):
	db = DataBase()
	x = db.get_playlists_by_id(int(_id))
	rep = {"run":True, "playlist": x}
	return render_template("index.html", **rep)


@app.route("/")
def home():
	query = request.args.get("search")
	play = request.args.get("play")
	fast_forward = request.args.get("ff")
	rewind = request.args.get("rewind")
	song = request.args.get("song_id")
	vibe = request.args.get("val")
	if vibe:
		session["vibe"] = vibe
	else:
		session["vibes"] = "0"

	ref = {"session":session}
	if play:
		if song:
			r = song_library.search_by_id(song)
			music_player.add_song(r)
		else:
			play_queue()
	elif song:
		r = song_library.search_by_id(song)
		music_player.remove_song()
		play_song(r)
	elif fast_forward:
		music_player.remove_song()
		music_player.stop()
		play_queue()
	elif rewind:
		if len(music_player.song_queue) > 0: 
			play_song(music_player.song_queue[0])
	elif query:
		results = song_library.search(query)
		ref = {"results":results, "search":query, "session":session}
	
	return render_template("index.html", **ref)
	

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