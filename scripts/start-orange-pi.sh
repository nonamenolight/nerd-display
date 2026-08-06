#!/bin/bash

set -e

PROJECT_DIR=/home/orangepi/project/nerd-display
LOG_FILE=$PROJECT_DIR/nerd-display.log

cd $PROJECT_DIR

source .venv/bin/activate

export SDL_VIDEODRIVER=kmsdrm

exec python main.py >> $LOG_FILE 2>&1
