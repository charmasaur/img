#!/usr/bin/env bash

if [ $# -ne 1 ] ; then
  echo "Usage: $(basename "$0") <filename>"
  exit
fi

url=$(curl -s -F "image=@$1" http://romper-image.appspot.com/upload) || { echo "Try again"; exit; }
echo $url
copy_commands=(xclip pbcopy)
for i in "${copy_commands[@]}" ; do
  hash $i 2>/dev/null && { printf $url | $i; echo "Copied to clipboard"; break; }
done
