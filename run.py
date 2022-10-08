from src.yotube_audio import AudioDownload
import asyncio
from time import perf_counter

if __name__ == '__main__':
    run =  AudioDownload()
    # run.get_from_youtube()
    start = perf_counter()
    run.load_urls('./urls.txt')
    print(perf_counter()-start)