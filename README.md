# Spotify Time Machine

# Overview
Spotify Time Machine is a Python script with a graphical user interface (GUI) built using Tkinter. It serves as a convenient tool for people who want to revisit the top songs on the Billboard Hot 100 chart from a specific date and create a personalized Spotify playlist based on those tracks.
  
# How It Works
- User Input: The user inputs a specific date in the provided entry field.
- Data Retrieval: The script scrapes the Billboard Hot 100 chart data for the given date, obtaining information about the top songs and artists.
- Spotify Connection: It connects to Spotify through Spotipy, utilizing the Spotify API to search for each song on Spotify.
- Playlist Creation: A private Spotify playlist is generated, containing the identified songs from the Billboard Hot 100 chart of the specified date.
- Feedback: The user receives confirmation messages via the GUI, indicating the successful creation of the Spotify playlist.
  
# Prerequisites
Before running the script, make sure you have the required Python libraries installed:
pip install requests beautifulsoup4 spotipy

# Usage
- Run the script.
- Enter the desired date in the provided entry field.
- Click the "Create Playlist" button.
- The script will generate a private Spotify playlist with the top songs from the specified date.
  
# Configuration
- Replace the placeholder values in the script (CLIENT ID, CLIENT SECRET, ACCESS TOKEN FILE PATH, and SPOTIFY USERNAME) with your actual Spotify developer credentials.
  
# Dependencies
- Tkinter
- Beautiful Soup
- Requests
- Spotipy


