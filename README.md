Spotify Time Machine
#Overview
Spotify Time Machine is a Python script with a graphical user interface (GUI) built using Tkinter. It allows users to generate a Spotify playlist based on the Billboard Hot 100 songs from a specific date.

Features
User Input: Enter the desired date in the format YYYY-MM-DD.
Web Scraping: Utilizes BeautifulSoup and requests to scrape Billboard Hot 100 data for the specified date.
Spotify Integration: Connects to Spotify via Spotipy, searches for songs on Spotify, and creates a private playlist.
Feedback: Provides feedback to the user about the playlist generation status.

Prerequisites
Before running the script, make sure you have the required Python libraries installed:
pip install requests beautifulsoup4 spotipy

Usage
Run the script.
Enter the desired date in the provided entry field.
Click the "Create Playlist" button.
The script will generate a private Spotify playlist with the top songs from the specified date.

Configuration
Replace the placeholder values in the script (CLIENT ID, CLIENT SECRET, ACCESS TOKEN FILE PATH, and SPOTIFY USERNAME) with your actual Spotify credentials.

Dependencies
Tkinter
Beautiful Soup
Requests
Spotipy
License

