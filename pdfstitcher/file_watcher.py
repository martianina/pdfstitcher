# file_watcher.py

import os
import glob
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

class MyHandler(FileSystemEventHandler):
    def __init__(self, main_frame):
        self.main_frame = main_frame

    def on_created(self, event):
        if event.is_directory:
            return

        print(f"New file created: {event.src_path}")
        # You can add additional logic here if needed
        self.main_frame.auto_load_newest_file()

    def start_file_watcher(self):
        """
        Start the file watcher to detect changes in the /uploads folder.
        """
        uploads_path = '/Users/ninakilbride/PDFStitcherWebApp/uploads'

        event_handler = MyHandler(main_frame=self)
        observer = Observer()
        observer.schedule(event_handler, path=uploads_path, recursive=False)

        try:
            observer.start()

            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()  # Ensure the observer thread is properly joined

