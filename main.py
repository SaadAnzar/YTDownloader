import os
import streamlit as st
from pytube import YouTube
from pytube import Playlist

def download_youtube_video(video_url):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        st.info(f"Downloading video: {yt.title}")
        video_stream.download()
        st.success(f"Download of '{yt.title}' completed!")
    except Exception as e:
        st.error(f"Error: {e}")

def download_playlist(playlist_url):
    try:
        playlist = Playlist(playlist_url)
        playlist_title = playlist.title

        st.info(f"Number of videos in playlist: {len(playlist.video_urls)}")

        # Create folder with playlist name
        folder_path = f"./{playlist_title}"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Download videos within the created folder
        os.chdir(folder_path)
        for video_url in playlist.video_urls:
            download_youtube_video(video_url)
    except Exception as e:
        st.error(f"Error: {e}")

def main():
    st.title("YouTube Video Downloader")

    # Input field for the YouTube video URL or playlist URL
    url = st.text_input("Enter YouTube Video/Playlist URL")

    # Download button
    if st.button("Download"):
        if "playlist?list=" in url:  # Check if it's a playlist URL
            download_playlist(url)
        elif url:
            download_youtube_video(url)
        else:
            st.warning("Please enter a YouTube video/playlist URL.")

if __name__ == "__main__":
    main()
