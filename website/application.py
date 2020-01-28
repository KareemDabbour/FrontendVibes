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

start = True
db = DataBase()
VIBES = ["HAPPY", "SAD", "ENERGETIC", "CALM"]

def update_names_and_queue():
    p1 = db.get_playlists_by_id("1")
    p2 = db.get_playlists_by_id("2")
    p3 = db.get_playlists_by_id("4")
    p4 = db.get_playlists_by_id("4")
    db.update_playlist(p1)
    db.update_playlist(p2)
    db.update_playlist(p3)
    db.update_playlist(p4)

    music_player.add_song(p1.songs[0])
    music_player.add_song(p1.songs[1])
    music_player.add_song(p1.songs[2])

    music_player.add_song(p2.songs[0])
    music_player.add_song(p2.songs[1])
    music_player.add_song(p2.songs[2])

    music_player.add_song(p3.songs[0])
    music_player.add_song(p3.songs[1])
    music_player.add_song(p3.songs[2])

    music_player.add_song(p4.songs[0])
    music_player.add_song(p4.songs[1])
    music_player.add_song(p4.songs[2])

    random.shuffle(music_player.song_queue)

update_names_and_queue()

@app.route("/playlist/<_id>")
def songs(_id):
    db = DataBase()
    x = db.get_playlists_by_id(int(_id))
    vibe = request.args.get("val")

    if vibe:
        session["vibe"] = vibe
    else:
        session["vibe"] = "0"

    rep = {"run":True, "playlist": x, "session":session}
    return render_template("index.html", **rep)


@app.route("/")
def home():
    query = request.args.get("search")
    play = request.args.get("play")
    fast_forward = request.args.get("ff")
    rewind = request.args.get("rewind")
    song = request.args.get("song_id")

    ref = {"session":session}
    if play:
        play_queue()
    elif song:
        r = song_library.search_by_id(song)
        music_player.remove_song()
        play_song(r)
    elif fast_forward:
        music_player.remove_song()
        music_player.remove_song()
        if len(music_player.song_queue) > 0:
            music_player.play(music_player.song_queue[0])
    elif rewind:
        if len(music_player.song_queue) > 0: 
            play_song(music_player.song_queue[0])
    elif query:
        print("Offline")
        """
        results = song_library.search(query)
        ref = {"results":results, "search":query, "session":session}"""
    
    return render_template("index.html", **ref)
    

def play_queue():
    if music_player.is_playing():
        pause()
    else:
        try:
            if start:
                start = False
                raise Exception()
            music_player.resume()
        except:
            if len(music_player.song_queue) > 0:
                play_song(music_player.song_queue[0])

    return redirect(url_for("home"))

def play_song(song):
    try:
        music_player.play(song)
    except:
        music_player.remove_song()
        if len(music_player.song_queue) > 0:
            music_player.play(music_player.song_queue[0])


def pause():
    try:
        music_player.pause()
    except:
        print("[LOG] Pleas start the music server")


if __name__ == "__main__":
    app.run(debug = True)