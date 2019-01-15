import argparse
from csv import reader
from datetime import datetime
from math import inf
from pprint import pprint
from types import SimpleNamespace

from youtube_utils.get_authenticated_service import get_authenticated_service
from youtube_utils.uploader import upload_video


def get_videofile_path(video, videosdir):
  created_date = datetime.fromisoformat(video['created_time'])
  date_slug = '{d.year}{d.month:02d}{d.day:02d}'.format(d=created_date)
  video_id = video['uri'].split('/')[-1]
  return '{0}/{1}-{2}/{2}.mp4'.format(videosdir, date_slug, video_id)

def get_privacy_status(video):
	return {
		'anybody': 'public',
		'disable': 'private',
		'nobody': 'private',
		'password': 'unlisted',
		'unlisted': 'unlisted',
	}[video['view_privacy']]

def get_video_category(video):
	return '29'

def format_video_data(video, videosdir):
	return {
		'categoryId': get_video_category(video),
		'defaultLanguage': 'English',
		'description': video['description'],
		'filepath': get_videofile_path(video, videosdir),
		'privacyStatus': get_privacy_status(video),
		'keywords': video['tags'],
		'title': video['name'],
	}

def is_uploaded(filepath):
	try:
		open('/'.join(filepath.split('/')[:-1] + ['.complete']))
		return True
	except FileNotFoundError:
		return False

def mark_uploaded(filepath):
	open('/'.join(filepath.split('/')[:-1] + ['.complete']), 'w')

def parse_and_upload_csv(youtube, file, videosdir, limit, offset):
	videos = []
	for f in file:
		with open(f, 'r') as csvfile:
			csv_reader = reader(csvfile, skipinitialspace=True)
			header = csv_reader.__next__()
			for video in csv_reader:
				videos.append(dict(zip(header, video)))

	videos = [
		format_video_data(v, videosdir) 
	for v in sorted(videos, key=lambda video: video['release_time'])]

	offset_count = 0
	count = 0
	for video in videos:
		if offset_count < offset:
			print('OFFSET')
			offset_count += 1
		elif count < limit:
			if not is_uploaded(video['filepath']):
				upload_video(youtube, SimpleNamespace(**video))
				mark_uploaded(video['filepath'])
			count += 1
		else:
			break

if __name__ == '__main__':
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--file", action='append', required=True, help="CSV file to read")
  argparser.add_argument("--videosdir", required=True, help="directory to videos")
  argparser.add_argument("--limit", default=inf, type=int, help="number of videos to upload")
  argparser.add_argument("--offset", default=0, type=int, help="number of videos to skip")
  args = argparser.parse_args()

  youtube = get_authenticated_service()
  parse_and_upload_csv(youtube, **args.__dict__)
