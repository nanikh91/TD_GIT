# game.py

import json
import random
from player_team import PlayerTeam
from enemy_team import EnemyTeam

class Game:
    history_file = "game_history.json"

    def __init__(self):
        self.__game_status = {
            "player_name": "",
            "action_context": "movement",
            "loot": 40,
            "player_team": None,
        }

    def config(self):
        player_name = input("Enter your name: ")
        self.__game_status["player_name"] = player_name
        self.__game_status["player_team"] = PlayerTeam([], 0, 0, 0, 0, 0, 0)
        self.__save_game_state()

    def status(self):
        print("Game Status:")
        print(f"Player: {self.__game_status['player_name']}")
        print(f"Loot: {self.__game_status['loot']}")
        print("Player Team:")
        if self.__game_status["player_team"]:
            print(f"Warriors: {self.__game_status['player_team'].get_nb_warriors()}")
            print(f"Hunters: {self.__game_status['player_team'].get_nb_hunters()}")
            print(f"Wizards: {self.__game_status['player_team'].get_nb_wizards()}")
        else:
            print("No player team yet.")
    
    def __load_player_team(self):
        with open(self.history_file, "r") as file:
            data = json.load(file)
            player_team_data = data.get("player_team", {})
            return PlayerTeam(
                members=[],
                nb_warriors=player_team_data.get("nb_warriors", 0),
                nb_hunters=player_team_data.get("nb_hunters", 0),
                nb_wizards=player_team_data.get("nb_wizards", 0),
                damage=player_team_data.get("damage", 0),
                loot=player_team_data.get("loot", 0),
                flee=player_team_data.get("flee", 0),
            )

    def __load_enemy_team(self):
        with open(self.history_file, "r") as file:
            data = json.load(file)
            enemy_team_data = data.get("enemy_team", {})
            return EnemyTeam(
                members=[],
                unit=enemy_team_data.get("unit", ""),
                damage=enemy_team_data.get("damage", 0),
                loot=enemy_team_data.get("loot", 0),
            )

    def player_damage(self):
        if self.__game_status["player_team"]:
            return self.__game_status["player_team"].get_damage()
        return 0

    def enemy_damage(self):
        enemy_team = self.__load_enemy_team()
        return enemy_team.get_damage()

    def load_game(self):
        with open(self.history_file, "r") as file:
            self.__game_status = json.load(file)

    def start_game(self):
        self.__game_status["action_context"] = "movement"
        self.__game_status["loot"] = 40
        self.__game_status["player_team"] = PlayerTeam([], 0, 0, 0, 0, 0, 0)
        self.__save_game_state()

    def buy(self, unit):
        if self.__game_status["action_context"] == "movement":
            # Vérifier si l'achat est possible et effectuer l'achat
            # Mettez à jour les données du fichier
            self.__save_game_state()
        else:
            print("You can only buy units during the movement context.")

    def move(self, direction):
        if self.__game_status["action_context"] == "movement":
            # Calculer le résultat du mouvement en fonction de la direction
            # Mettez à jour les données du fichier
            self.__save_game_state()
        else:
            print("You can only move during the movement context.")

    def fight(self):
        if self.__game_status["action_context"] == "combat":
            # Simuler le combat et mettre à jour les données du fichier
            self.__save_game_state()
        else:
            print("You can only fight during the combat context.")

    def flee(self):
        if self.__game_status["action_context"] == "combat":
            # Simuler la fuite et mettre à jour les données du fichier
            self.__save_game_state()
        else:
            print("You can only flee during the combat context.")

    def __save_game_state(self):
        with open(self.history_file, "w") as file:
            json.dump(self.__game_status, file)

    def __update_loot(self, value):
        self.__game_status["loot"] += value
        self.__save_game_state()