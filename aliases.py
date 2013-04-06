import os
import subprocess

import common

class Aliases:
    file_name = '~/.config/sting/aliases'

    def __init__(self):
        self.items = []
        self.readConfig()

    def readConfig(self):
        for name, command in common.readConfig(Aliases.file_name):
            self.items.append((name, command))

    def search(self, search_text):
        return list(common.filter(search_text, self.items))

    # run is called when user execute a command (aka press Enter)
    def run(self, match_item):
        subprocess.Popen([match_item.command])
    