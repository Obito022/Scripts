import yt_dlp as youtube_dl


def get_video(url, output_path="."):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(artist)s - %(title)s.%(ext)s",
        "format": "bestaudio/best",
        "writethumbnail": True,  # Download thumbnail
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {
                "key": "EmbedThumbnail",  # Embed thumbnail
                "already_have_thumbnail": False,
            },
        ],
        "postprocessor_args": [
            "-id3v2_version",
            "3",  # Use ID3v2.3 for better compatibility
            "-ar",
            "48000",
        ],
        "prefer_ffmpeg": True,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download and conversion completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_directory = (
        input("Enter the output directory (leave blank for current directory): ") or "."
    )
    get_video(video_url, output_directory)
