import argparse
import json

'''
python parse_description.py --file="../videos/20180809-284219793/284219793.info.json"
'''

def load_file(filename):
  with open(filename, 'r') as myfile:
    data = myfile.read()
    return json.loads(data)
  return {}

if __name__ == '__main__':
  argparser = argparse.ArgumentParser()
  argparser.add_argument("--file", required=True, help="JSON file to read")
  args = argparser.parse_args()

  d = load_file(args.file)
  print json.dumps(d, indent=2)
