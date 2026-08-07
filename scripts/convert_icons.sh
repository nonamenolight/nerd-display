#!/bin/bash

set -e

SRC_DIR="assets/icons/svg"
DST_DIR="assets/icons/png"

SIZE=512

mkdir -p "$DST_DIR"

for svg in "$SRC_DIR"/*.svg
do
    filename=$(basename "$svg" .svg)

    echo "Converting $filename..."

    rsvg-convert \
        -w $SIZE \
        -h $SIZE \
        "$svg" \
        -o "$DST_DIR/$filename.png"
done

echo "Done!"
