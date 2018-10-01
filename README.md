# youtube-uploader

Epic is migrating its message videos from Vimeo to YouTube.

This [Vimeo Downloader](https://github.com/epicsf/vimeo-downloader/)
gets all the video IDs/names/descriptions and other metadata,
and downloads the original video file.

This takes the message videos and updates them to YouTube using
[YouTube's API](https://developers.google.com/youtube/v3/guides/uploading_a_video).

[API docs](https://developers.google.com/youtube/v3/docs/videos)

## Dependencies

```
sudo pip install google-api-python-client
sudo pip install oauth2client
```

## Client Secrets

https://developers.google.com/youtube/v3/guides/authentication

https://developers.google.com/youtube/registering_an_application

Set up credentials: https://console.cloud.google.com/apis/dashboard?project=epicsfyoutubeuploaded
Used http://localhost:8080/ as the Redirect URL

Create a `client_secrets.py` file in the same folder as the script, but DO NOT add it to Github.

## Disclaimer

Followed the instructions from [here](https://developers.google.com/youtube/v3/guides/uploading_a_video).

## Running the script

In the same folder as where the `uploader.py` script is:
```
python uploader.py --file="../videos/20180809-284219793/284219793.mp4"
```

While the script is running, check [here](https://www.youtube.com/my_videos) or [here](https://studio.youtube.com/) to monitor progress.

## Setting the publish date

No option for this. See [here](https://productforums.google.com/forum/#!msg/youtube/uaNfcNFHx84/lZ_dJh1nDAAJ).
