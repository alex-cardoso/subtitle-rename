import os
from os import listdir
import re

extensions_accepted = ['.avi', '.mp4', '.srt', '.mkv']


def separate_movie_and_subtitles():
    home = os.path.expanduser('~')
    downloads = os.path.join(home, 'Downloads')
    files = listdir(str(downloads + '/test_organizer'))
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
    return {filename: filename, 'movies': movies_file, 'subtitles': subtitles_file, 'path': downloads + '/test_organizer/'}


def rename(season, episodes, files):
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
                            str(files['path']+str(subtitle)), str(files['path']+str(filename)+'.srt'))
                        print(movie)


files = separate_movie_and_subtitles()
rename('09', 24, files)
