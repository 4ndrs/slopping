# slopping
A script to make cropping easy when ffmpeg'ing. Needs slop, libxdo (xdotool), and xwininfo.

## Usage
```console
$ ffmpeg -i input -vf crop=$(slopping) output
```

[slopping_and_ffmpeg.webm](https://user-images.githubusercontent.com/31898900/180082865-dfd17cc2-be30-433d-a6ef-dc1f575510d4.webm)

The window we are hovering with the mouse needs to be of the same size (w, h) of the video to extract the correct values.

To generate PIL.Image cropping coordinates, pass 'pil' as argument when executing the script: 
```console
$ slopping pil
```

Can also be imported as a module to query the coordinates:
```python
[ins] In [1]: import slopping

[ins] In [2]: ffmpeg_crop = slopping.crop()

[nav] In [3]: pil_crop = slopping.crop('pil')

[ins] In [4]: ffmpeg_crop
Out[4]: (244, 210, 128, 228)

[ins] In [5]: pil_crop
Out[5]: (309, 367, 554, 484)
```

## Installation

```console
$ pip install slopping
```
