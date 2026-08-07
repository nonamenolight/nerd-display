#!/bin/bash

set -e

SRC_DIR="assets/icons/svg"
DST_DIR="assets/icons/png"

HEIGHT=512

mkdir -p "$DST_DIR"

for svg in "$SRC_DIR"/*.svg
do
    filename=$(basename "$svg" .svg)

    # 转换文件名:
    # 空格 -> -
    # 大写 -> 小写
    # 连续特殊字符处理
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
