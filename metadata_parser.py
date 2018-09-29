import argparse
import csv

'''
python metadata_parser.py --file="../videos/vimeo_export_epicsf_2018-09-03T170913-0700.csv"
'''

def load_file(filename):
  headers = []

  with open(filename, 'r') as csvfile:
    myreader = csv.reader(csvfile, skipinitialspace=True)
    for i, row in enumerate(myreader):
      print row
      print i

if __name__ == '__main__':
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--file", required=True, help="JSON file to read")
  args = argparser.parse_args()

  d = load_file(args.file)
  print d

