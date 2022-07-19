#!/usr/bin/env python3
# Copyright (c) 2022 4ndrs <andres.degozaru@gmail.com>
# SPDX-License-Identifier: MIT
"""A script to make cropping easy when ffmpeg'ing.
   Needs slop, xdotool, and xwininfo.

   Usage: ffmpeg -i input -vf crop=$(slopping) output"""

from subprocess import check_output
import re

if __name__ == "__main__":
    CROP = check_output(["slop", "-f", "%w %h %x %y"]).decode()
    CROP = tuple(int(n) for n in CROP.split())  # (w, h, x, y)

    # The mouse pointer needs to be hovering the video we are cropping
    WINDOW_ID = check_output(["xdotool", "getmouselocation", "--shell"])
    WINDOW_ID = re.search(rb".*WINDOW=(\d+)", WINDOW_ID).groups()[0]

    WINDOW_XY = check_output(["xwininfo", "-id", WINDOW_ID]).decode()
    WINDOW_XY = tuple(
        int(n)
        for n in re.search(
            r"Absolute.*X:\s+(\d+).*Absolute.*Y:\s+(\d+)", WINDOW_XY, re.DOTALL
        ).groups()
    )

    CROP_XY = CROP[2:]

    # CROP_X - WINDOW_X, CROP_Y - WINDOW_Y
    CROP_XY = tuple(c - w for c, w in zip(CROP_XY, WINDOW_XY))
    CROP = CROP[:2] + CROP_XY

    # Print format without newline for ffmpeg: w:h:x:y
    SEPARATOR = ":"
    for i, n in enumerate(CROP):
        print(n, end="")
        if i < 3:
            print(SEPARATOR, end="")
