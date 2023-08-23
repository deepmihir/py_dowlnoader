from pytube import Playlist
import re  # Import the regular expressions module

# Define a function to clean the title
def clean_filename(title):
    # Remove all characters that are not letters, numbers, spaces, or underscores
    cleaned_title = re.sub(r'[^\w\s]', '', title)
    return cleaned_title

# Define the playlist URL
playlist_url = input("Enter Youtube Plalist URL:")

# Create a Playlist object
p = Playlist(playlist_url)

print(f'Downloading: {p.title}')

# Iterate through the videos in the playlist
for index, video in enumerate(p.videos):
    # Get the highest resolution stream
    highest_res_stream = video.streams.get_highest_resolution()
    
    # Clean the video title
    cleaned_title = clean_filename(video.title)
    
    # Append index to the cleaned title
    modified_title = f"{index + 1}_{cleaned_title}.mp4"
    
    # Download the video with the modified title
    highest_res_stream.download(filename=modified_title)
    
    print(f'Downloaded: {modified_title}')
