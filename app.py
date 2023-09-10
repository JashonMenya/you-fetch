from flask import Flask, request, redirect, url_for
from pytube import YouTube
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key


def remove_downloads_dir():
    """
     Function to remove the 'my-downloads' directory if it exists.
    :return: Deletes the folder contents in preparation for new downloads
    """
    downloads_dir = os.path.join(os.getcwd(), 'my-downloads')
    if os.path.exists(downloads_dir):
        for root, dirs, files in os.walk(downloads_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(downloads_dir)


def download_file(youtube_url, download_type):
    """
    Function to handle the download process
    :param youtube_url: YouTube link for what needs to be downloaded
    :param download_type: file format needed. audio or video
    :return: the downloaded file format requested
    """
    try:
        yt = YouTube(youtube_url)
        if download_type == 'video':
            stream = yt.streams.get_highest_resolution()
            file_extension = stream.mime_type.split('/')[-1]
        elif download_type == 'audio':
            stream = yt.streams.filter(only_audio=True).first()
            file_extension = 'mp3'  # You can specify the desired audio file extension here
        else:
            print('Invalid download type', 'error')
            return redirect(url_for('index'))

        video_title = re.sub(r'[\/:*?"<>|]', '', yt.title)
        filename = f"{video_title}.{file_extension}"

        downloads_dir = os.path.join(os.getcwd(), 'my-downloads')
        os.makedirs(downloads_dir, exist_ok=True)

        filepath = os.path.join(downloads_dir, filename)
        stream.download(output_path=downloads_dir, filename=filename)

        print('You download should be ready, check the my-downloads folder')
    except Exception as e:
        print(e)
        print(f'Error: {str(e)}', 'error')


# Route to handle the main functionality
@app.route('/you-fetch', methods=['GET', 'POST'])
def index():
    """
    Main runner
    :return: Your Flask application is running
    """
    if request.method == 'POST':
        remove_downloads_dir()  # Remove the existing 'my-downloads' directory

        data = request.json
        youtube_url = data.get('youtube_url')
        download_type = data.get('download_type')

        if not youtube_url:
            print('Please enter a YouTube URL', 'error')
            return redirect(url_for('index'))

        download_file(youtube_url, download_type)

    return "Your Flask application is running."


if __name__ == '__main__':
    app.run(debug=True)
