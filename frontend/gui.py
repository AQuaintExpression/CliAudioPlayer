from PyInquirer import style_from_dict, prompt, Separator
from examples import custom_style_1, custom_style_2, custom_style_3
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    return prompt({
        'type': 'list',
        'name': 'func_handler',
        'message': 'Main Menu',
        'choices': [
            Separator(),
            'Search Song',
            'Search Playlist',
            'Stop Player',
        ]
    }, style=custom_style_3)

def single_song_menu():
    cls()
    return prompt({
        'type': 'list',
        'name': 'func_handler',
        'message': 'Song Menu',
        'choices': [
            Separator(),
            'Play',
            'Pause',
            'Stop',
            'Play Next',
            'Search Another',
            'Search Playlist'
            'Main Menu',
        ]
    }, style=custom_style_1)


if __name__ == '__main__':
    print(main_menu())
    print(single_song_menu())

