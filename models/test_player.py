from player import Player
from song_library import SongLibrary

p = Player()
lib = SongLibrary()
commands = ["PLAY", "PAUSE", "RESUME"]

while True:
	command = input("Command: ")
	if command in commands:
		if command == "PLAY":
			song = input("Type a song: ")
			response = lib.search(song)

			p.play(response[0])

		elif command == "PAUSE":
			p.pause()
		else:
			p.resume()
	else:
		p.pause()
		break
