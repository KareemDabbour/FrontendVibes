Simple music player (WAV/OGG) written in python with pygame

## Instructions for Linux

### Dependencies
- docker >= 19.03.5

### Building the project and starting the player
Run `./bin/build-image`. After it's done, run `./bin/run-player` to start.
The HTTP API will be available on `localhost:8080`.

---

## Instructions for OSX / Windows

### Dependencies (Mac OSX)
- vagrant >= 2.2.6
- virtualbox <= 6.0 (6.1 won't work)

### Dependencies (Windows)
- GitBash
- vagrant >= 2.2.6
- virtualbox <= 6.0 (6.1 won't work)

[Download VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_6_0)

[Download Vagrant](https://www.vagrantup.com/downloads.html)

[Download GitBash (for Windows)](https://git-scm.com/downloads)

### Building the project (Mac OSX / Windows)
Since we can't easily share the audio devices on a OSX or Windows hosts, this
project comes with a Vagrantfile to run everything inside a Virtual Machine.

#### Starting and provisioning the Vagrant box
Run `vagrant up` and when it is done, run `vagrant reload` so it restarts the VM
and reloads the audio drivers. Then, to connect to the VM, simply run `vagrant
ssh`

#### Building the project image and starting the player
Once inside the VM (`vagrant ssh`), run `./bin/build-image` and
`./bin/run-player` to start the API. From now on, all endpoints will be
accessible on `localhost:8080`, even from outside the VM.

### Troubleshooting
#### No music playing
Check the audio volume and the selected audio device.

#### No audio devices (OSX / Windows)
You're probably using a non-standard audio card, so you need to change the audio
controller. Open the `Vagrantfile` and at line `67`, change the controller to
match the correct one. For `AC97`, change the `audiocontroller` value from `hda`
to `ac97`. And for `soundblaster`, change it to `sb16`.
Then do `vagrant reload` and it will load the new controller.

#### Vagrant VM freezes (OSX / Windows)
Do a `vagrant reload` to restart the VM.

---

## Starting the player
Every time you start the player, it will ask you for the Card ID. That is the ID
of your soundcard. It will load a list of available devices and you have to
choose the correct one. Look for devices that are NOT `HDMI`. If you choose one
and it doesn't work, simply restart the player and pick another one :) **In most
cases, the correct choice will be `0` or the device with `Analog` in its name.**

---

## Controlling the player
You can control the player using the HTTP API listening on port 8080.

### POST /play - Play songs
Play by `name` (local file) or by `url` (download and play).

Parameters (one or the other, name has precedence):
- name
- url

Play by name:
`curl -X POST localhost:8080/play?name=cantina-band.wav`

Play by url:
`curl -X POST localhost:8080/play?url=<asset-url>`

**Playing by URL will cause the song to be cached, so it is available to be
played by name**

### POST /stop - Stop music playback
`curl -X POST localhost:8080/stop`

### POST /pause - Pause music playback
`curl -X POST localhost:8080/pause`

### POST /unpause - Unpause music playback
`curl -X POST localhost:8080/unpause`

### POST /download - Cache a music file
It will download the asset and cache it under the `music` directory. So it is
available to be played using the `name` parameter.

`curl -X POST localhost:8080/download?url=<asset-url>`

### GET /status - Get player status
It will return `playing` if it's playing or paused and `idle` if it's not
playing nor paused.

`curl localhost:8080/status`
