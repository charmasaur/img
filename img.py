#!/bin/python
import json, requests, sys

if not len(sys.argv) == 2:
    print("Usage: img <filename>")
    sys.exit()

filename = str(sys.argv[1])
try:
    f = open(filename, "rb")
except IOError:
    print("Failed to open " + filename)
    sys.exit()

result = requests.post("https://api.imgur.com/3/image", headers={"Authorization":"Client-ID c0e6d83a72d02a9"}, files={"image":f}).json()

if result["success"]:
    print(result["data"]["link"])
else:
    print("Something went wrong, status code " + str(result["status"]))
