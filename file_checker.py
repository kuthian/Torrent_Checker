# uses the qbitTorrent client API found here: https://github.com/v1k45/python-qBittorrent
# uses source code obtained from here: http://timgolden.me.uk/python/win32_how_do_i/watch_directory_for_changes.html,
# Documentation for the API can be found here: http://python-qbittorrent.readthedocs.io/en/latest/?badge=latest
from qbittorrent import Client
import os
import time


def main():
    qb = Client('http://127.0.0.1:8080/')
    qb.login()

    paths = dict([(f, None) for f in os.listdir(".")])

    if "watch_path" in paths:
        watch_path_f = open('watch_path')
        watch_path = watch_path_f().read()
    else:
        watch_path_f = open("watch_path.txt", "w+")
        watch_path_f.write(".")
        watch_path = "."
    watch_path_f.close()
    if "download_save_path" in paths:
        download_save_path_f = open('download_save_path')
        download_save_path = download_save_path_f().read()
    else:
        download_save_path_f = open("download_save_path.txt", "w+")
        download_save_path_f.write(".")
        download_save_path = "."

    download_save_path_f.close()

    original_files_in_path = dict([(f, None) for f in os.listdir(watch_path)])

    while 1:
        time.sleep(15)
        current_files_in_path = dict([(f, None) for f in os.listdir(watch_path)])
        new_files_in_path = [f for f in current_files_in_path if f not in original_files_in_path]
        removed_files_in_path = [f for f in original_files_in_path if f not in current_files_in_path]
        if new_files_in_path:
            print("Added: ", ", ".join(new_files_in_path))
            for f in new_files_in_path:
                try:
                    file_with_magnet_link = open(f)
                    qb.download_from_link(file_with_magnet_link.read(), savepath=download_save_path)
                    file_with_magnet_link.close()
                    torrents = qb.torrents(filter='downloading')
                    for torrent in torrents:
                        print("Downloading: " + torrent['name'])
                        open(torrent['name'] + " - Downloading.txt", "w+")

                        os.remove(f)
                except ValueError:
                    print("Error reading magnet link.")
                except:
                    print("Unexpected error")

        if removed_files_in_path:
            print("Removed: ", ", ".join(removed_files_in_path))

        torrents = qb.torrents(filter='seeding')
        for torrent in torrents:
            print("Completed: " + torrent['name'])
            qb.pause(torrent['hash'])
            open(torrent['name'] + " - Completed.txt", "w+")

        original_files_in_path = dict([(f, None) for f in os.listdir(watch_path)])


if __name__ == "__main__":
    main()
