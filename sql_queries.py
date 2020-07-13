import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "staging_events"
staging_songs_table_drstaging_songsop = "songplays"
songplay_table_drop = ""
user_table_drop = "users"
song_table_drop = "songs"
artist_table_drop = "artists"
time_table_drop = "time"

# CREATE TABLES
 
staging_events_table_create= ("""  CREATE TABLE IF NOT EXISTS    staging_events (artist text, auth text, firstName text, gender text, itemInSession int,lastName text, length float, level text,location text, method text,page text, registration float, sessionId int, song text,status int, ts  int, userAgent text ,userId int)   PRIMARY KEY (sessionId, userId )                                   
""")

staging_songs_table_create = (""" CREATE TABLE IF NOT EXISTS    staging_songs (artist_id text, artist_latitude text, artist_location text, artist_longitude text, artist_name text, duration float, num_songs int, song_id text, title text, year int) PRIMARY KEY ( artist_id, song_id)                                       
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

songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id , level, song_id, artist_id, session_id, location,  user_agent) VALUES( %, %, %, %, %, %, %, %, %);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)VALUES( %, %, %, %, %);
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES( %, %, %, %, %);
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, lattitude, longitude) VALUES( %, %, %, %, %);
""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES( %, %, %, %, %, %, %);
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
