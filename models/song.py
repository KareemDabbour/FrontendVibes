class Song:
	def __init__(self, name, _id, artist, duration, genre):
		self.name = name
		self.id = _id
		self.artist = artist
		self.genre = genre
		self.duration = duration

	def __repr__(self):
		return f"Song(Name: {self.name}, Artist: {self.artist}, Duration: {self.duration})"

