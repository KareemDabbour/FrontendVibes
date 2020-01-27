class Song:
	def __init__(self, name, _id, artist, duration, genre):
		self.name = name
		self.id = str(_id)
		self.artist = artist
		self.genre = genre
		self.duration = self.second_to_min(duration)

	def second_to_min (self, duration):
		mn, sec = divmod(duration, 60) 
		return "%02d:%02d" % (mn, sec)

	def __repr__(self):
		return f"Song(Name: {self.name}, Artist: {self.artist}, Duration: {self.duration})"

