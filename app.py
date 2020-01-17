import os
import re
from pathlib import Path

external = str(input('Estao em HD externo? s/n: '))
path = str(input('Qual o diretorio: '))
season = str(input('Qual temporada: '))
episodes = int(input('Numero de episodios: '))

directory = path.strip() if external == 's' else str(Path.home())+path

if len(season) != 2:
    print('A temporada tem que ter 2 caracteres, se for menor que 10, use o 0 antes, como 01, 02..etc..')
    exit()

if not os.path.isdir(directory):
    print('Diretório '+directory+' não existe')
    exit()

files = os.listdir(directory)

extensions_accepted = ['.avi', '.mp4', '.srt', '.mkv']


def separate_movie_and_subtitles():

    movies_file = []
    subtitles_file = []

    for file in files:
        if not file.startswith('.'):
            filename, file_extension = os.path.splitext(file)
            if file_extension not in extensions_accepted:
                print('File not accept '+file_extension)
            else:
                if file_extension == '.srt':
                    subtitles_file.append(file)
                else:
                    movies_file.append(file)
    return {filename: filename, 'movies': movies_file, 'subtitles': subtitles_file}


def rename(files):
    for episode in range(1, episodes+1):
        if episode < 10:
            episode = '0'+str(episode)

        season_and_episode_format = 'S'+str(season)+'E'+str(episode)

        for movie in sorted(files['movies']):
            if re.search(season_and_episode_format, movie.upper()):
                filename, file_extension = os.path.splitext(movie)
                movie_string = season_and_episode_format
                for subtitle in sorted(files['subtitles']):
                    if re.search(movie_string, subtitle.upper()):
                        os.rename(
                            str(directory+'/'+subtitle), str(directory+'/'+filename)+'.srt')
                        print(movie)


files = separate_movie_and_subtitles()
rename(files)
