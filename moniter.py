import os
import sys
import time
from threading import Thread
from queue import Queue

import win32file
import win32con


def moniter():
    ACTIONS = {
    1: "+", # create
    2: "-", # delete
    3: "*", # update
    4: "<", # rename
    5: ">"  # rename to
    }

    FILE_LIST_DIRECTORY = 0x0001

    path_to_watch = 'D:/work/file_moniter/test/'
    print('Watching changes in', path_to_watch)
    hDir = win32file.CreateFile(
    path_to_watch,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
    )
    while 1:
        time.sleep(1)
        results = win32file.ReadDirectoryChangesW(
            hDir,
            1024,
            True,
            win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
            win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
            win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
            win32con.FILE_NOTIFY_CHANGE_SIZE |
            win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
            win32con.FILE_NOTIFY_CHANGE_SECURITY,
            None,
            None)
        for action, filename in results:
            time_str = time.strftime('%Y%m%d%H%M')
            print(f'{time_str} {ACTIONS.get(action, "?")} {filename}')
            # full_filename = os.path.join(path_to_watch, filename)
            # print(full_filename, ACTIONS.get(action, "Unknown"))

if __name__ == '__main__':
    moniter()
