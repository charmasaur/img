#!/usr/bin/env bash

if [ $# -ne 1 ] ; then
  echo "Usage: $(basename "$0") <filename>"
  exit
fi

curl -F "image=@$1" http://romper-image.appspot.com/upload
echo
