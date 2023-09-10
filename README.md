# You Fetch Downloader

## Table of Contents

- [Set Up](#set-up)
  - [Install Postman](#install-postman)
  - [Clone the Repository](#clone-the-repository)
  - [Set Up and Activate a Virtual Environment](#set-up-and-activate-a-virtual-environment)
  - [Install Dependencies to the Virtual Environment](#install-dependencies-to-the-virtual-environment)
  - [Start the App Locally](#start-the-app-locally)
- [Using Postman to Download YouTube Videos/Audio](#using-postman-to-download-youtube-videos-and-audio)
- [SKIP POSTMAN](#skip-postman)

---

## Set Up

### Install Postman

1. **Install Postman**: If you haven't already, [download and install Postman](https://www.postman.com/downloads/).

### Clone the Repository

2. **Clone the Repository**: Clone this GitHub repository to your local machine using the following command:
   ```bash
        git clone https://github.com/JashonMenya/you-fetch.git
   ````

3. **Set Up and Activate a Virtual Environment**
    ```
    cd you-fetch
    python -m venv venv
    venv/Scripts/activate
    ```

4. **Install Dependencies to the Virtual Environment**
    ```
        pip install -r requirements.txt
    ```

5. **Start the App Locally**
    ```
        python app.py
    ```

6. **Using Postman to Download YouTube Videos and Audio**
    Install Postman**: If you haven't already, [download and install Postman](https://www.postman.com/downloads/).

        **Open Postman**
        - Launch Postman on your computer.

        **Create a POST Request**:
        - Click on the "New" button in Postman to create a new request.
        - Choose "POST" as the request method.
        - Enter the URL where your Flask app is running. By default, it's `http://localhost:5000/you-fetch`.

        **Set the Request Body**:
        - In the request body section, select "raw" and choose "JSON (application/json)" as the content type.
        - Copy and paste the following JSON into the request body:
            ```json
            {
                "youtube_url": "https://youtu.be/SbDxnXS-hrE?si=YZgyVXgSJoATDg-X",
                "download_type": "audio"
            }
            ```
        - Adjust the `"youtube_url"` and `"download_type"` values as needed.

        **Send the Request**:
        - Click the "Send" button in Postman to make the POST request to your Flask app.

        **Check the Flask App Output**:
        - Go back to your terminal where the Flask app is running. You should see output related to the download process.
        - If the request is successful, you will see a message like "You download should be ready, check the my-downloads folder in this projects you-fetch/my-downloads".

    That's it! You've successfully used Postman to trigger your Flask application to download a YouTube video or audio locally.

7. **Skip Postman**

    You can SKIP using postman by replacing  
    ```
    youtube_url = data.get('youtube_url')
    download_type = data.get('download_type')
    ```
    with
    
    ```
    youtube_url = "your url"
    download_type = "your download type(audio or video)"
    ```
    in app.py. Line 55 and 56