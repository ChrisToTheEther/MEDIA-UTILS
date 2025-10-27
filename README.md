# Utilities For Creating Media 

## Start:

```bash
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Tools:

- toBitmap.py: Converts png to bitmap
- toPixel.py: Adds Pixel effect an downscales png or .jpeg 
- yt_audio.py: Gets Audio from YouTube video as .wav or mp3 (requires ffmpeg on machine)



FruitJam supports 16bit PCM sample width = 2 bytes audio
for now to get a .wav onto the fruitjam use:
if the yt_audio.py fix does not work for .wav conversion use:
```bash
ffmpeg -i input.wav -ac 1 -ar 11025 -acodec pcm_s16le output.wav
```

