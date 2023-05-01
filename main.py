#!/bin/python

# --------------------------------------------------------------
# Copyright (C) 2023: Snyder Business And Technology Consulting. - All Rights Reserved
#
# Licensing:
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# Date:
# April 29, 2023
#
# Author:
# Alexander Snyder
#
# Email:
# alexander@sba.tc
#
# Repository:
# https://github.com/thisguyshouldworkforus/imdb-search
#
# Dependency:
# PyMovieDb
#
# Description:
# See README.md
# --------------------------------------------------------------

# Import the modules
from omdbapi.movie_search import GetMovie
import re
import os

# Get the API Key
file_path = "./secret/omdb.api"
with open(file_path, "r") as file:
    for line in file:
        if not line.startswith('#'):
            OMDB_API = line.strip()

# Instantiate the class
imdb = GetMovie(api_key=f'{OMDB_API}')

# Get the list of all files and directories
PATHS = ["P:\\movies", "P:\\disney", "P:\\documentaries", "P:\\hallmark"]
for PATH in PATHS:
    FOLDERS = os.listdir(PATH)
    for FOLDER in FOLDERS:
        if '{' not in FOLDER or '}' not in FOLDER:
            FOLDER_NAME = re.sub(r'\.?\d{4}\.?$', '', FOLDER).replace('.', ' ').replace('- ', ' - ')
            # Search the Open Movie Database
            try:
                IMDB_SEARCH = imdb.get_movie(title=f'{FOLDER_NAME}')
                IMDB_SEARCH_YEAR = str(IMDB_SEARCH['year'])
                IMDB_YEAR = re.match(r"^([0-9]{4})(.*)", IMDB_SEARCH_YEAR).group(1)
                OUTPUT = (f"{IMDB_SEARCH['title']} ({IMDB_YEAR}) %%imdb-{IMDB_SEARCH['imdbid']}@@").replace('%%', '{').replace('@@', '}').replace(':', ' - ').replace('  ', ' ').replace('*', '-').replace('?', '')
                print(f"Working: '{PATH}\\{FOLDER}' --> '{PATH}\\{OUTPUT}'")
                #os.rename(f'{PATH}\\{FOLDER}', f'{PATH}\\{OUTPUT}')
            except TypeError:
                #print(f"Encountered error on: {FOLDER_NAME}")
                print('',end='')
