import yt_dlp
from pydub import AudioSegment
import os

def youtube_to_audio(url, output_format='mp3', output_folder='downloads'):
    os.makedirs(output_folder, exist_ok=True)

    # Temp audio download
    temp_file = os.path.join(output_folder, "temp_audio.webm")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': temp_file,
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        title = info.get('title', 'audio')

    # Convert with pydub
    audio = AudioSegment.from_file(temp_file)
    output_path = os.path.join(output_folder, f"{title}.{output_format}")
    
    if output_format == 'mp3':
        audio.export(output_path, format='mp3', bitrate='192k')
    elif output_format == 'wav':
        audio.export(
        output_path,
        format='wav',
        parameters=['-acodec', 'pcm_s16le', '-ac', '1', '-ar', '11025']
    )
    else:
        raise ValueError("Output format must be 'mp3' or 'wav'")

    os.remove(temp_file)
    print(f"Saved: {output_path}")
    return output_path

#https://www.youtube.com/watch?v=A8wK-vhuWog, https://www.youtube.com/watch?v=miZHa7ZC6Z0
#run
youtube_to_audio("https://www.youtube.com/watch?v=A8wK-vhuWog", output_format="wav")
