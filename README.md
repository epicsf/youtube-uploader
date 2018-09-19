# youtube-uploader

Epic is migrating its message videos from Vimeo to YouTube.

This [Vimeo Donwloader](https://github.com/epicsf/vimeo-downloader/)
gets all the video IDs/names/descriptions and other metadata,
and downloads the original video file.

This takes the message videos and updates them to YouTube using
[YouTube's API](https://developers.google.com/youtube/v3/guides/uploading_a_video).

## Dependencies

```
sudo pip install google-api-python-client
sudo pip install oauth2client
```

## Client Secrets

https://developers.google.com/youtube/v3/guides/authentication

https://developers.google.com/youtube/registering_an_application

Create a `client_secrets.py` file in the same folder as the script, but DO NOT add it to Github.

## Disclaimer

Followed the instructions from [here](https://developers.google.com/youtube/v3/guides/uploading_a_video).

## Running the script

In the same folder as where the `uploader.py` script is:
```
python uploader.py --file="../videos/20180809-284219793/284219793.mp4"
```
