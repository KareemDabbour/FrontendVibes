#!/usr/bin/env python

import os
import pygame
import wget
import pwd
import grp
import random
import string


class Player:
    def __init__(self):
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=8096)
        pygame.mixer.init()
        self.source_path = '{}/music/'.format(os.getenv('APP_PATH'))

    def play(self, file_name):
        song_path = self.source_path + file_name

        if os.path.exists(song_path):
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()

            return True
        else:
            return False

    def stop(self):
        pygame.mixer.music.stop()

        return True

    def pause(self):
        pygame.mixer.music.pause()

        return True

    def unpause(self):
        pygame.mixer.music.unpause()

        return True

    def status(self):
        return pygame.mixer.music.get_busy()

    def download(self, url):
        # Generate a random name for the file
        file_name = self._generate_file_name()
        file_path = self.source_path + file_name

        # check if file exists and return if it does
        if os.path.exists(file_path):
            print('File already exists. Skipping the download')
            return file_name

        print('Downloading file:', file_name)
        wget.download(url, out='{}{}'.format(self.source_path, file_name))

        # change ownership
        os.chown(
            file_path,
            pwd.getpwnam(os.getenv('APP_USER')).pw_uid,
            grp.getgrnam(os.getenv('APP_USER')).gr_gid
        )

        return file_name

    def _generate_file_name(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(32))
