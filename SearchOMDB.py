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
# OMDB API
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
omdb = GetMovie(api_key=f'{OMDB_API}')

# Get the list of all files and directories
PATHS = ["P:\\movies", "P:\\disney", "P:\\documentaries", "P:\\hallmark"]
for PATH in PATHS:
    FOLDERS = os.listdir(PATH)
    for FOLDER in FOLDERS:
        if '{' not in FOLDER or '}' not in FOLDER:
            FOLDER_NAME = FOLDER.replace('.', ' ').replace('- ', ' - ')
            # Search the Open Movie Database
            try:
                OMDB_SEARCH = omdb.get_movie(title=f'{FOLDER_NAME}')
                if OMDB_SEARCH:
                    OMDB_SEARCH_YEAR = str(OMDB_SEARCH['year'])
                    if OMDB_SEARCH_YEAR:
                        OMDB_YEAR = re.match(r"^([0-9]{4})(.*)", OMDB_SEARCH_YEAR).group(1)
                        if OMDB_YEAR:
                            OUTPUT = (f"{OMDB_SEARCH['title']} ({OMDB_YEAR}) %%imdb-{OMDB_SEARCH['imdbid']}@@").replace('%%', '{').replace('@@', '}').replace(':', ' - ').replace('  ', ' ').replace('*', '-').replace('?', '')
                            print(f"Working: '{PATH}\\{FOLDER}' --> '{PATH}\\{OUTPUT}'")
                            #os.rename(f'{PATH}\\{FOLDER}', f'{PATH}\\{OUTPUT}')
                        else:
                            print('Failed to find a YEAR match')
                    else:
                        print('Failed to SEARCH for YEAR in FOLDER')
                else:
                    print(f"Failed to find a match for '{FOLDER_NAME}'")
            except TypeError:
                #print(f"Encountered error on: {FOLDER_NAME}")
                print('',end='')