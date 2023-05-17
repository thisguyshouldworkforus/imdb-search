#!/usr/bin/env python

# --------------------------------------------------------------
# Copyright (C) 2023: Snyder Business And Technology Consulting. - All Rights Reserved
#
# Licensing:
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# Date:
# May 16, 2023
#
# Author:
# Alexander Snyder
#
# Email:
# alexander@sba.tc
#
# Repository:
# https://github.com/thisguyshouldworkforus/python
#
# Dependency:
# TVDB API Key
#
# Description:
# Search The TV Database for show IDs and rename collection accordingly
# --------------------------------------------------------------

import requests
import os
import json
import re

# Get the Bearer Token
token_file_path = "./secret/token"
with open(token_file_path, "r") as file:
    for line in file:
        BEARER_TOKEN = str(line.strip())

BASE_URL = "https://api4.thetvdb.com/v4"

TV_PATHS=["P:\\tv.shows", "P:\\tv.docs", "P:\\tv.kids"]

for PATH in TV_PATHS:
    FOLDERS = os.listdir(PATH)
    for FOLDER in FOLDERS:
        if 'XXXXXX' in FOLDER:
            QUERY = (FOLDER.split('(', 1)[0]).strip()

            ENDPOINT = f"/search?query='{QUERY}'"

            # Form the full URL
            url = BASE_URL + ENDPOINT

            # Include the bearer token in the headers
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer {}'.format(BEARER_TOKEN)
            }

            # Make the request
            response = requests.get(url, headers=headers)

            # The response of the request can be read as json
            response_data = response.json()

            TVDB_ID = (response_data['data'][0]['tvdb_id']).strip()
            NEW_FOLDER = re.sub('XXXXXX', TVDB_ID, FOLDER)

            print(f"Old Folder: {FOLDER}\nNew Folder: {NEW_FOLDER}\n")
            try:
                os.rename(f'{PATH}\\{FOLDER}', f'{PATH}\\{NEW_FOLDER}')
            except PermissionError:
                print(f"Permission Error on: {PATH}\\{FOLDER} --> {PATH}\\{NEW_FOLDER}")
