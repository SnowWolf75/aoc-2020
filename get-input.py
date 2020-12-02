#!/usr/bin/env python3
import argparse
import subprocess
import requests
import shutil
from datetime import datetime
from pytz import timezone
import pytz

utc_dt = datetime.utcnow().replace(tzinfo=pytz.utc)
eastern = timezone('US/Eastern')
east_coast = utc_dt.astimezone(eastern)
cur_day = east_coast.day
cur_year = east_coast.year
print("Current UTC:",utc_dt)
print("Current datetime:",east_coast)

parser = argparse.ArgumentParser(description='Read Input for Advent of Code')
parser.add_argument('--day', type=int, default=cur_day)
parser.add_argument('--year', type=int, default=cur_year)
args = parser.parse_args()

cook = {"session":"53616c7465645f5f2fe87f1f28d923619de5147b6153f73a8289af449a48dbde29ceb8526c50c422dadfe0108f4b0018"}
url = "https://adventofcode.com/{}/day/{}/input".format(args.year, args.day)

res = requests.get(url, cookies=cook)

if res.status_code == 200:
  outfile = "inputs/{0:04d}_12_{1:02d}_input.txt".format( args.year, args.day )
  with open(outfile, "w") as fh:
    fh.write( str( res.text.strip() ) )
  print("Input text fetched and saved:",outfile)

# https://adventofcode.com/2019/day/8/input

stub = 'stub.py'
newfile = "{:02d}.py".format(args.day)
shutil.copy(stub, newfile)

myday = "{:02d}".format(args.day)
template = """
filename = "{2}"
class day{0}:
  def __init__(self):
    pass


class day{0}part1(day{0}):
  def solve(self, args):
    pass


class day{0}part2(day{0}):
  def solve(self, args):
    pass


class examples(unittest.TestCase):
  def test_examples_part1(self):
    day{1} = day{0}part1()
    # self.assetTrue()

  def test_examples_part2(self):
    day{1} = day{0}part2()
    # self.assetTrue()


class solutions(unittest.TestCase):
  def test_part1(self):
    day{1} = day{0}part1()

  def test_part2(self):
    day{1} = day{0}part2()
""".format(myday, args.day, outfile)

with open(newfile, "a+") as fh:
  fh.write( template )
