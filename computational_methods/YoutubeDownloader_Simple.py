import os
import pytube
from pytube import Playlist
from pytube import Channel
from pytube import YouTube
from datetime import datetime

def download_video(url, output_path):
    print(f"Downloading video: {url}")
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution().download(output_path)
        print(f"Video '{yt.title}' downloaded successfully.")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_playlist(url, output_path):
    print(f"Downloading playlist: {url}")
    try:
        playlist = Playlist(url)
        for video_url in playlist.video_urls:
            download_video(video_url, output_path)
    except Exception as e:
        print(f"Error downloading playlist: {e}")

def download_channel(url, output_path):
    print(f"Downloading channel: {url}")
    try:
        channel = Channel(url)
        for video_url in channel.video_urls:
            download_video(video_url, output_path)
    except Exception as e:
        print(f"Error downloading channel: {e}")

def main():
    url = input("Enter the YouTube video, playlist, or channel URL: ")
    output_path = os.path.join(os.getcwd(), "downloads")
    os.makedirs(output_path, exist_ok=True)

    if "watch" in url:
        download_video(url, output_path)
    elif "playlist" in url:
        download_playlist(url, output_path)
    elif "channel" in url or "user" in url:
        download_channel(url, output_path)
    else:
        print("Invalid URL.")

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Script started at: {start_time}")
    main()
    end_time = datetime.now()
    print(f"Script finished at: {end_time}")
    print(f"Total time taken: {end_time - start_time}")
