from models import start_music


if __name__ == "__main__":
	try:
		start_music.start_player()
		print("Music server has been started.")
	except:
		print("Could't start the Music server on port 8080.")