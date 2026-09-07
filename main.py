# Music Playlist Manager Project
# begginning of the project
import time
playlists = {}
while True:
    print('Welcome to the Playlist Manager!')
    print()
    print('1 - Create a playlist')
    print('2 - Go to a playlist already created')
    print('3 - View playlists')
    print('4 - Exit')
    print()

# Where the user chooses what option he wants:
    user = (input('Please choose an option: '))
    print()

# Where is if the user chose an option that is not valid:
    if user not in ['1', '2', '3', '4']:
        print('Invalid option, please choose a valid option!'.upper())
        print()

# Continuing the code if the user chose a valid option:
    elif user == '1':
        time.sleep(1)
        print('Creating a new playlist...')
        print()
        time.sleep(1)
        playlist_name = (input('Please enter the name of your playlist: '))
        music_list = []
        print()
        playlists[playlist_name] = music_list
        print(f'Playlist {playlist_name} created!')
        print()
        
        musics = (input('Please enter the name of the music you want to add to your playlist: '))
        music_list.append(musics)
        time.sleep(1)
        print()
        print('Music added to your playlist!') 
        print()

#Showing the user the playlist created and the music added:
        print(f'Playlist: {playlist_name}')
        for number, music in enumerate(music_list, start=1):
            print(f'{number} - {music}')
        print()

        while True:
            user2 = input('Would you like to add another music? ').upper()
            print()

            if user2 not in ['YES', 'NO']:
                print('INVALID OPTION, PLEASE CHOOSE A VALID OPTION!'.upper())
                print()
            elif user2 == 'YES':
                new_music = (input('Please enter the name of the new music: '))
                print()
                music_list.append(new_music)
                print()
                for number, music in enumerate(music_list, start=1):
                    print(f'{number} - {music}')
                print()
                print(f'Music {new_music} added to your playlist!')
                print()
            elif user2 == 'NO':
                time.sleep(1)
                print('Going back to the main menu...')
                time.sleep(2)
                print()
                break
    elif user == '2':
        print('Going to a playlist already created...')
        print()
        time.sleep(1)
        print('Here are your playlists:')
        print()
        for playlist in playlists:
            print(f'- {playlist}')
        print()

        playlist_name = input (str('Enter the name of the playlist you want to edit: '))
        print()
        time.sleep(1)
        if playlist_name not in playlists:
            print('Playlist not found!')
            print()
            time.sleep(1)
            continue


        music_list = playlists[playlist_name]

        print('1 - Add a music')
        print('2 - Remove a music')
        print('3 - Rename the playlist')
        print('4 - Back to the main menu')
        print()
        edit_option = input('Please choose an option: ')

        if edit_option not in ['1', '2', '3', '4']:
                print('Invalid option, please choose a valid option!'.upper())
                print()

        elif edit_option == '1':
            new_music = input('Enter the name of the music you want to add: ')
            print()
            music_list.append(new_music)
            print(f'Music {new_music} added to your playlist!')
            print()
            print(f'Playlist: {playlist_name}')
            for number, music in enumerate(music_list, start=1):
                print(f'{number} - {music}')
                print()
        elif edit_option == '2':
            print(f'Playlist: {playlist_name}')
            for number, music in enumerate(music_list, start=1):
                print(f'{number} - {music}')
            print()
            remove_music = input('Enter the number of the music you want to remove: ')
            print()
            if not remove_music.isdigit():
                print('Invalid option')
                print()
            else: 
                remove_music = int(remove_music)

                if remove_music < 1 or remove_music > len(music_list):
                    print('Invalid music number')
                    print()
                else:
                    remove = music_list.pop(remove_music - 1)
                    print(f'"{remove}" removed successfully!')
                    print()
        elif edit_option == '3':

            new_name = input('Enter the new playlist name: ')
            print()
            playlists[new_name] = playlists.pop(playlist_name)
            playlist_name = new_name
            print(f'Playlist renamed to {new_name}!')
            print()

            print(f'Playlist: {playlist_name}')
            for number, music in enumerate(music_list, start=1):
                print(f'{number} - {music}')
            print()
            print('Playlist updated!')
            print()

        elif edit_option == '4':
            time.sleep(1)
            print('Going back to the main menu...')
            time.sleep(2)
            print()
        
    elif user == '3':
        print('Here are your playlists:')
        print()
        time.sleep(1)
        for playlist in playlists:
            print(f'- {playlist}')
        show_playlist = input('\nPress Enter to return to the main menu...')
    elif user == '4':
        time.sleep(1)
        print('Goodbye!')
        time.sleep(1)
        break
   
