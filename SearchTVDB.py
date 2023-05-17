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

import tvdb_v4_official

# Get The TVDB API
api_file_path = "./secret/tvdb.api"
with open(api_file_path, "r") as file:
    for line in file:
        TVDB_API = str(line.strip())

# Get The TVDB Key
pin_file_path = "./secret/tvdb.pin"
with open(pin_file_path, "r") as file:
    for line in file:
        TVDB_PIN = str(line.strip())

print(f"TVDB Pin: {TVDB_PIN}")
print(f"TVDB API: {TVDB_API}")

tvdb = tvdb_v4_official.TVDB(TVDB_API)

# IMDB ID for TV Show '1883'
tvdb.search_by_remote_id(remoteid='tt13991232')