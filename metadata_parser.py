import argparse

'''
python metadata_parser.py --file="../videos/vimeo_export_epicsf_2018-09-03T170913-0700.csv"
'''

def load_file(filename):
  with open(filename, 'r') as myfile:
    for line in myfile:
      print '\n\n ***'
      print line

if __name__ == '__main__':
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--file", required=True, help="JSON file to read")
  args = argparser.parse_args()

  d = load_file(args.file)
  print d

