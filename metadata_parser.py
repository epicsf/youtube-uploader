import argparse
import csv

'''
python metadata_parser.py --file="../videos/vimeo_export_epicsf_2018-09-03T170913-0700.csv"
'''

def load_file(filename):
  headers = []

  with open(filename, 'r') as csvfile:
    myreader = csv.reader(csvfile, skipinitialspace=True)
    header = myreader.next()
    for i, session in enumerate(myreader):
        name = session[1]
        description = session[2]
        privacy = session[7]
        tags = session[9]

        print '\n **** '
        print 'name: %r' % name
        print 'description: %r' % description
        print 'privacy: %r' % privacy
        print 'tags: %r' % tags


if __name__ == '__main__':
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--file", required=True, help="JSON file to read")
  args = argparser.parse_args()

  d = load_file(args.file)
  print d

