#!/usr/bin/env python
import json, requests, sys

if not len(sys.argv) == 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit()

filename = str(sys.argv[1])
try:
    f = open(filename, "rb")
except IOError:
    print("Failed to open " + filename)
    sys.exit()

response = requests.post("https://romper-image.appspot.com/upload", files={"image":f})

print(response.text)
