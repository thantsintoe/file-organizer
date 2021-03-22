import os
import time
import shutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

folderToTrack = "/Users/thantsintoe/Downloads"
folderDistination = "/Users/thantsintoe/Downloads/NEW"

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def on_created(event):
    for filename in os.listdir(folderToTrack):
        src = folderToTrack + "/" + filename
        if(os.path.isdir(src)):
            continue
        if (filename.endswith('.png') or filename.endswith('.jpg')):
            folder = 'Pictures'
        elif (filename.endswith('.zip') or filename.endswith('.tar.gz')):
            folder = 'Zip'
        elif (filename.endswith('.pdf') or filename.endswith('.epub')):
            folder = 'Books'
        elif (filename.endswith('.dmg')):
            folder = 'Programs'
        elif (filename.endswith('.pdf')):
            folder = 'Books'
        elif (filename.endswith('.mp4')):
            folder = 'Videos'
        else:
            folder = 'General'
        create_folder_if_not_exists(folderToTrack + "/" + folder)
        dist = folderToTrack + "/" + folder + "/" + filename
        try:
            shutil.move(src, dist)
        except Exception:
            print("An error happened")
            print(Exception)
myHandler = FileSystemEventHandler()
myHandler.on_created = on_created

observer = Observer()
observer.schedule(myHandler, folderToTrack, recursive=True)
observer.start()

try:
    print("Observing")
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
