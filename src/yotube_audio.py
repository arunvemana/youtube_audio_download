from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

import concurrent.futures

TEMP_FILE = 'temp'
OUTPUT_FILE = 'output'


class AudioDownload:
    @staticmethod
    def get_from_youtube(url):
        data = YouTube(url).streams.get_highest_resolution().download(TEMP_FILE)
        filename, _ = (os.path.splitext(os.path.basename(data)))
        video = VideoFileClip(data)
        audio = video.audio
        audio.write_audiofile(f"{OUTPUT_FILE}/{filename}.mp3")
        return filename

    @staticmethod
    def remove_temp_files():
        for filename in os.listdir(TEMP_FILE):
            filepath = os.path.join(TEMP_FILE, filename)
            if os.path.isfile(filepath):
                os.unlink(filepath)

    def load_urls(self, filename: str):
        try:
            with open(filename) as f:
                urls = f.readlines()
            with concurrent.futures.ThreadPoolExecutor() as ex:
                tasks = [ex.submit(self.get_from_youtube, url.replace('\n', '')) for url in urls]
            for i in concurrent.futures.as_completed(tasks):
                print(f"done with {i.result()}")
        except Exception as e:
            print(e)
        self.remove_temp_files()
