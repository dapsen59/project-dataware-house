import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = ""
staging_songs_table_drop = "songplays"
songplay_table_drop = ""
user_table_drop = "users"
song_table_drop = "songs"
artist_table_drop = "artists"
time_table_drop = "time"

# CREATE TABLES
 
staging_events_table_create= ("""  CREATE TABLE IF NOT EXISTS    staging_events                                        
""")

staging_songs_table_create = (""" CREATE TABLE IF NOT EXISTS    staging_songs                                        
""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id text, start_time int, user_id int, level text, song_id int, artist_id int, session_id int, location text  user_agent text) PRIMARY KEY (user_id) 
""")

user_table_create = ("""  CREATE TABLE IF NOT EXISTS users (user_id int, first_name text, last_name text, gender text, level text) PRIMARY KEY(user_id)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (song_id text, title text, artist_id text, year int, duration int) PRIMARY KEY(song_id, artist_id)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id text, name text, location text, lattitude text, longitude text) PRIMARY KEY(artist_id)
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time int, hour int, day text, week text, month text, year int, weekday text ) PRIMARY KEY(weekday)
""")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
