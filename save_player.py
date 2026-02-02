"""Setting up file handling for saving players"""

import os
import constants as cons


class SavePlayer():
    """Saved players"""
    def __init__(self):
        if not os.path.exists(cons.FILE_NAME):
            with open(cons.FILE_NAME,"w", encoding="utf-8"):
                pass

    def load_players(self):
        """Loads the past players"""
        players = {}
        with open(cons.FILE_NAME,"r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    name, level = line.split(",",1)
                    players[name.strip()] = int(level.strip())
                except ValueError:
                    continue
        return players

    def save_player(self, name: str, level: int):
        """Add/update player level in file"""
        players = self.load_players()
        players[name] = level

        with open(cons.FILE_NAME, "w", encoding="utf-8") as f:
            for player_name, lvl in players.items():
                f.write(f"{player_name},{lvl}\n")

    def gets_player(self,name:str):
        """Gets level if player exists"""
        players = self.load_players()
        level = players.get(name)
        if level is None:
            return 0
        return level
