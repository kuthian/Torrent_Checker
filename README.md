# Torrent_Checker
A Python script that checks a folder for txt files containing magnet links and downloads them to a specified folder. Works with qbbittorent.

Edit the path text files (watch_path and download_save_path) with the desired path you wish to monitor and the path where you wish the 
completed download to be placed. If the files are not present, run the script once to generate them. 

Start qbittorrent (tested with v4.0.3) and run the script.

Copy the magnet link for your chosen torrent into an empty .txt file and add it to the watch_path. TorrentChecker will then consume the
file and create a file called Your_Torrent_Name - Downloading.txt to indicated that downloading has begun. When the download is complete,
a new file named Your_Torrent_Name - Completed.txt will be generated. The download will then be available in your donwload_save_path.
