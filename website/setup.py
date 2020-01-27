from models.player import Player
from models.song_library import SongLibrary 
from models.database import DataBase
from models.song import Song
import random
import glob, os, os.path

def delete_music():
    PATH = os.getcwd() + "/models/music/music/"

    filelist = glob.glob(os.path.join(PATH, "*"))
    for f in filelist:
        os.remove(f)

    print("REMOVED OLD FILES")


def create_playlist(db, music_player):
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



def setup_playlist():
    #delete_music()
    pass
