from flask import Flask, render_template, url_for, redirect, request
from models import Player, SongLibrary


app = Flask(__name__)
music_player = Player()
song_library = SongLibrary()

@app.route('/')
def home():
	return render_template("index.html")

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