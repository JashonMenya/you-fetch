from flask import Flask, request, redirect, url_for, flash
from pytube import YouTube
import os
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

@app.route('/you-fetch', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Remove the existing 'my-downloads' directory at the beginning of each request
        remove_downloads_dir()

        data = request.json
        youtube_url = data.get('youtube_url')
        download_type = data.get('download_type')

        if not youtube_url:
            flash('Please enter a YouTube URL', 'error')
            return redirect(url_for('index'))

        try:
            yt = YouTube(youtube_url)
            if download_type == 'video':
                stream = yt.streams.get_highest_resolution()
            elif download_type == 'audio':
                stream = yt.streams.filter(only_audio=True).first()
            else:
                flash('Invalid download type', 'error')
                return redirect(url_for('index'))

            # Sanitize the title for use as a filename
            video_title = re.sub(r'[\/:*?"<>|]', '', yt.title)
            file_extension = stream.mime_type.split('/')[-1]
            filename = f"{video_title}.{file_extension}"

            # Create a 'my-downloads' folder within your project directory
            downloads_dir = os.path.join(os.getcwd(), 'my-downloads')
            os.makedirs(downloads_dir, exist_ok=True)

            # Update the filepath to point to the 'my-downloads' folder
            filepath = os.path.join(downloads_dir, filename)
            stream.download(output_path=downloads_dir, filename=video_title)

            flash('Download completed successfully!', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            print(e)
            flash(f'Error: {str(e)}', 'error')

    return "Your Flask application is running."

def remove_downloads_dir():
    # Remove the 'my-downloads' directory if it exists
    downloads_dir = os.path.join(os.getcwd(), 'my-downloads')
    if os.path.exists(downloads_dir):
        for root, dirs, files in os.walk(downloads_dir, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(downloads_dir)

if __name__ == '__main__':
    app.run(debug=True)
