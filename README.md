# slopping
Usage: ffmpeg -i input -vf crop=$(slopping) output

[slopping_and_ffmpeg.webm](https://user-images.githubusercontent.com/31898900/180082865-dfd17cc2-be30-433d-a6ef-dc1f575510d4.webm)

The window we are hovering with the mouse needs to be of the same size (w, h) of the video to extract the correct values.

To generate a PIL.Image crop tuple, pass 'pil' as argument when executing the script: slopping pil
