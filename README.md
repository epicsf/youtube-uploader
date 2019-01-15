# Youtube Uploader

This python script is the second of two scripts for transferring videos from Vimeo to Youtube. The first can be found [here](https://github.com/epicsf/vimeo-downloader/).

## Notes

This script is based off of the Youtube examples found [here](https://github.com/youtube/api-samples/blob/master/python/upload_video.py).

Youtube API Docs can be found [here](https://developers.google.com/youtube/v3/docs/videos).

## Setup

This script has been written and tested with Python version 3.7.

To install:

#### 1. Install Dependencies
Run `pip install -r requirements.txt`.

#### 2. Create Client Secrets
1. Go to [https://console.developers.google.com](https://console.developers.google.com/) and, if necessary, create a new project. If creating a new project, make sure to also set up the OAuth consent screen.
2. Click on "ENABLE APIS AND SERVICES" and search for (and enable) "Youtube Data API v3".
3. In the project, create an "OAuth client ID" credential and download the created JSON file
4. Name the file "client_secret.json" and place in the root level of the repository


## Running the script

*Note:* This script keeps track of which videos it has uploaded before by adding a `.complete` file in the video directory of videos it has uploaded.
To re-upload videos, delete the `.complete` file.

To run the script, run:
```
python main.py --file <path/to/csv/file.csv> --videosdir <path/to/videos/directory>
```

The script takes the following arguments
`--file` - The location of the csv file paths. Multiple files can be specified.
					 The script will combine all the csv files and sort them by release date.
`--videosdir` - The directory where the videos are stored. Only one source directory is allowed.
`--limit` (Optional) - The number of videos to upload.
`--offset` (Optional) - The number of videos to skip initially.

While the script is running, check [here](https://www.youtube.com/my_videos) or [here](https://studio.youtube.com/) to monitor progress.

