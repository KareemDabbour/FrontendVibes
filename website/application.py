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
print(db.get_all_playlists())

def create_playlist():
    p1 = db.create_playlist("HAPPY", "HAPPY")
    s = SongLibrary()

    x = s.search("Dancing Queen")[0]
    p1.add_song(x)
    x = s.search ("Walking on Sunshine")[0]
    p1.add_song(x)
    x = s.search ("Happier")[0]
    p1.add_song(x)
    x = s.search ("All Star")[0]
    p1.add_song(x)
    x = s.search ("Hey, Soul Sister")[0]
    p1.add_song(x)
    db.update_playlist(p1)

    p2 = db.create_playlist("SAD","SAD")
    s2 = SongLibrary()

    x = s.search("Strawberry Swing")[0]
    p2.add_song(x)
    x = s.search ("Blem")[0]
    p2.add_song(x)
    x = s.search ("Signs")[1]
    p2.add_song(x)
    x = s.search ("Peace")[0]
    p2.add_song(x)
    db.update_playlist(p2)


    p3 = db.create_playlist("ENERGETIC","ENERGETIC")
    x = s.search("Marvin's Room")[0]
    p3.add_song(x)
    x = s.search ("These Walls")[0]
    p2.add_song(x)
    x = s.search ("Take me to church")[1]
    p3.add_song(x)
    x = s.search ("Broken")[0]
    p3.add_song(x)
    x = s.search ("Orlando")[0]
    p3.add_song(x)
    db.update_playlist(p3)

    p4 = db.create_playlist("CALM","CALM")
    x = s.search("Trophies")[0]
    p4.add_song(x)
    x = s.search ("Life is Good")[1]
    p4.add_song(x)
    x = s.search ("DNA")[0]
    p4.add_song(x)
    x = s.search ("Humble")[0]
    p4.add_song(x)
    x = s.search ("Nonstop")[0]
    p4.add_song(x)
    db.update_playlist(p4)



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
    try:
        print(session["vibe"])
    except:
        pass

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
        results = song_library.search(query)
        ref = {"results":results, "search":query, "session":session}
    
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
        if len(music_player) > 0:
            music_player.play(music_player.song_queue[0])


def pause():
    try:
        music_player.pause()
    except:
        print("[LOG] Pleas start the music server")


if __name__ == "__main__":
    app.run(debug = True)