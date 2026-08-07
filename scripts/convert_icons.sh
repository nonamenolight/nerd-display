#!/bin/bash

set -e

SRC_DIR="assets/icons/svg"
DST_DIR="assets/icons/png"

HEIGHT=512

mkdir -p "$DST_DIR"

# 清理旧 png
rm -f "$DST_DIR"/*.png

for svg in "$SRC_DIR"/*.svg
do
    filename=$(basename "$svg" .svg)

    output=$(echo "$filename" \
        | sed 's/ /-/g' \
        | tr '[:upper:]' '[:lower:]')

    echo "Converting $filename.svg -> $output.png"

    rsvg-convert \
        -h $HEIGHT \
        "$svg" \
        -o "$DST_DIR/$output.png"

done

echo "Done!"
