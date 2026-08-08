"""
CLI-скрипт: скачивает список файлов по URL из текстового файла и складывает
их в целевую папку. Запускается вручную инженером. Лежит в scripts/downloader.py.
"""

import os
import sys
import requests


def download_all(urls_file, target_dir):
    urls = open(urls_file).read().split("\n")

    for url in urls:
        filename = url.split("/")[-1]
        path = os.path.join(target_dir, filename)

        try:
            r = requests.get(url)
            f = open(path, "wb")
            f.write(r.content)
            f.close()
            print("Downloaded " + filename)
        except:
            print("Failed " + url)
            continue


if __name__ == "__main__":
    urls_file = sys.argv[1]
    target_dir = sys.argv[2]
    download_all(urls_file, target_dir)
