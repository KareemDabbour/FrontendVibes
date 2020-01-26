from flask import Flask, render_template, url_for, redirect
from models import Player, SongLibrary


app = Flask(__name__)
music_player = Player()
song_library = SongLibrary()

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/play/<song>")
def play(song):
	try:
		sng = song_library.search(song)[0]
		music_player.play(sng)
	except:
		print("[LOG] Please start the music server")

	return redirect(url_for("home"))

@app.route("/pause")
def pause():
	try:
		music_player.pause()
	except:
		print("[LOG] Pleas start the music server")

	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug = True)