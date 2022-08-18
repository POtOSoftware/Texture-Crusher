import subprocess
import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--keep", default=False, action='store_true')
parser.add_argument("--verbose", default=False, action='store_true')
args, leftovers = parser.parse_known_args()

try:
    filename = sys.argv[1]
    outputfilename = sys.argv[2]
    resolution = sys.argv[3]

    subprocess.call(['ffmpeg', '-i', filename, '-vf', 'scale=' + resolution, outputfilename])

    if args.keep is False:
        os.remove(filename)
except Exception as error:
    print("Usage: texturecrusher [input] [output] [WIDTHxHEIGHT]")
    if args.verbose:
        print(error)
