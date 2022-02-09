from frontend.gui import main_menu, cls
from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def main(previous_media=''):
    signal(SIGINT, handler)
    cls()
    if previous_media:
        print(previous_media)
    choice = main_menu()

    if choice['func_handler'] == 'Search Song':
        current_media = input('\nEnter Song name: ')
        print(current_media, 'Calling play song method')

    if choice['func_handler'] == 'Search Playlist':
        current_media = input('\nEnter Playlist name: ')
        print(current_media, 'Calling play Playlist method')

    if choice['func_handler'] == 'Stop Player':
        print(' Stopping Player')
        exit(0)
    main(current_media)
    

if __name__ == "__main__":
    main()
