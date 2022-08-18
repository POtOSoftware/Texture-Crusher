import subprocess
import sys
import os

try:
    filename = sys.argv[1]
    outputfilename = sys.argv[2]
    resolution = sys.argv[3]

    subprocess.call(['ffmpeg', '-i', filename, '-vf', 'scale=' + resolution, outputfilename])
    os.remove(filename)
except:
    print("Usage: texturecrusher [input] [output] [WIDTHxHEIGHT]")
