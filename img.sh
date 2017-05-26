#!/usr/bin/env bash

if [ $# -ne 1 ] ; then
  echo "Usage: $(basename "$0") <filename>"
  exit
fi

url=$(curl -s -F "image=@$1" http://romper-image.appspot.com/upload) || { echo "Try again"; exit; }
echo $url
hash xclip 2>/dev/null && { printf $url | xclip; echo "Copied to clipboard"; }
