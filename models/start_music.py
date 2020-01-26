import os
import socket

def check_port():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('localhost',8080))
	sock.close()
	return result == 0

def start_player():
	if not check_port:
		print("Server is already running on this port. Exiting")
	else:
		try:
			cwd = os.getcwd()
			os.chdir(cwd + "/music") 
			os.system("./bin/run-player")
		except:
			raise Exception("Could not start player.")


if __name__ == "__main__":
	start_player()
