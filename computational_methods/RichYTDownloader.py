import os
import pytube
from pytube import Playlist, Channel, YouTube
from datetime import datetime
from rich.progress import Progress, TaskID

def download_video(url, output_path, progress):
    print(f"Downloading video: {url}")
    try:
        yt = YouTube(url, on_progress_callback=progress.update)
        video = yt.streams.get_highest_resolution()
        video_size = video.filesize
        video_title = yt.title

        progress_bar_1 = progress.add_task("[green]Downloading...", total=1)
        progress_bar_2 = progress.add_task(f"[cyan]{video_title}", total=video_size)

        video.download(output_path)

        progress.update(progress_bar_1, advance=1)
        progress.update(progress_bar_2, advance=video_size)

        print(f"Video '{video_title}' downloaded successfully.")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_playlist(url, output_path):
    print(f"Downloading playlist: {url}")
    try:
        playlist = Playlist(url)
        playlist_name = playlist.title
        playlist_path = os.path.join(output_path, playlist_name)
        os.makedirs(playlist_path, exist_ok=True)
        with Progress() as progress:
            task = progress.add_task(f"[yellow]Downloading {playlist_name}", total=len(playlist.videos))
            while not progress.finished:
                for video_url in playlist.video_urls:
                    download_video(video_url, playlist_path, progress)
                    progress.update(task, advance=1)
    except Exception as e:
        print(f"Error downloading playlist: {e}")

def download_channel(url, output_path):
    print(f"Downloading channel: {url}")
    try:
        channel = Channel(url)
        with Progress() as progress:
            task = progress.add_task(f"[magenta]Downloading channel", total=len(channel.videos))
            while not progress.finished:
                for video_url in channel.video_urls:
                    download_video(video_url, output_path, progress)
                    progress.update(task, advance=1)
    except Exception as e:
        print(f"Error downloading channel: {e}")

def main():
    url = input("Enter the YouTube video, playlist, or channel URL: ")
    output_path = os.path.join(os.getcwd(), "downloads")
    os.makedirs(output_path, exist_ok=True)

    if "watch" in url:
        with Progress() as progress:
            download_video(url, output_path, progress)
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
