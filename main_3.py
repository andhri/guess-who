import json
from game_logic_v4 import ArtGame
from game_inferface_v5 import GameInterface
from game_answers import GameAnswers
from game_options import ArtOptions
from display import DisplayConfig
from parent_interface import Parent


# class GameRun:
# add an exception here for when the file fails to load, load another file
""" Loading data in the game """
def load_data():
    try:
        file_name = "game_data_clean.json"
        with open(file_name, 'r') as database:
            data = json.load(database)
            return data
    except FileNotFoundError:
        file_name = "game_data_clean.json"
        with open(file_name, 'r') as database:
            data = json.load(database)
            return data

# load_data()

# id = data[random.randrange(len(data))]["objectID"]
# print(id)
# check_index = [id == i['objectID'] for i in data].index(True)
# print(check_index)


""" Running the game program """
def run_game():
    play = ArtGame(load_data())
    parent = Parent()
    display = DisplayConfig(parent, play)
    answers = GameAnswers(parent, play, display)
    art_options = ArtOptions(parent, play, display)
    play_game = GameInterface(parent, play, art_options, answers, display)
    return play_game


if __name__ == '__main__':
    run_game()
# print(play.check_year())