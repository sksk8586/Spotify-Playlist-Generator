from  tkinter import *
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import datetime

GREEN = "#1db954"
BLACK = "#121212"
GRAY = "#b3b3b3"

FONT_NAME = "Century"

def get_info():
    date = date_entry.get()
    string_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%B %Y")
    url = f"https://www.billboard.com/charts/hot-100/{date}/"

    response = requests.get(url)
    data = response.text

    #scraping billboard hot 100 and creating a list of top songs
    soup = BeautifulSoup(data, "html.parser")
    title = soup.select("li ul h3")
    artists = soup.select("li ul span" )

    song_names = [i.get_text().strip() for i in title]

    year = date.split("-")[0]

    #authorization to spotify
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id= "abb1ec20138848b08f3695cda37af590",
            client_secret="ebcdca5b51274cdfb110a057523309a0",
            show_dialog=True,
            cache_path="token.txt",
            username="sk",
        )
    )

    user_id = sp.current_user()
    tracks_uri_list = []
    #getting uris of each song from song list
    for i in song_names:

        try:
            id = sp.search(q=f"track:{i} year:{year}", type="track")
            something = id["tracks"]["items"][0]["uri"]
            tracks_uri_list.append(something)
        except IndexError:
            pass
    #creating playlist
    o = sp.user_playlist_create(user = "31ltn54zj7unezmbscs7jgfu6iw4", name = f"Hits from {string_date} ", public= False,
                             description="sharvi's playlist 1")

    #adding to song playlist via song uri
    sp.playlist_add_items(items= tracks_uri_list, playlist_id= o["id"],position=None)

    confirm = Label(text= "Playlist Generated", font=(FONT_NAME, 20), fg=GREEN, bg=BLACK)
    confirm.grid(column=1, row=5)

#-------------------------UI-------------------------------------------
window = Tk()
window.title("Spotify Time Machine")
window.config(bg = BLACK, pady=100, padx=100)


title = Label(text = "Spotify Time Machine", font = (FONT_NAME,50), fg = GREEN, bg = BLACK)
title.grid(column=1,row = 0)

prompt = Label(text = "Which year would you like to hear from? YYYY-MM-DD:", font = (FONT_NAME,20), fg = GRAY, bg = BLACK)
prompt.grid(column=1,row = 1)


date_entry = Entry(width = 40)
date_entry.grid(row = 2, column = 1, columnspan=2, pady=20)

generate = Button(text = "Create Playlist", width= 50, command= get_info)
generate.grid(columnspan=2, row = 3, pady= 20)



window.mainloop()

