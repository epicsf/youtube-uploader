# youtube-uploader

Epic is migrating its message videos from Vimeo to YouTube.

This [Vimeo Donwloader](https://github.com/epicsf/vimeo-downloader/)
gets all the video IDs/names/descriptions and other metadata,
and downloads the original video file.

This takes the message videos and updates them to YouTube using
[YouTube's API](https://developers.google.com/youtube/v3/guides/uploading_a_video).

## Dependencies

```
pip3 install --upgrade google-api-python-client
```

## Client Secrets

Create a `client_secrets.py` file in the same folder as the script, but DO NOT add it to Github.

## Disclaimer

Followed the instructions from [here](https://developers.google.com/youtube/v3/guides/uploading_a_video).
