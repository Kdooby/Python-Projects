
import shutil
import os
import time





seconds_in_day = 24 * 60 * 60
# The time it is now
now = time.time()

# The time it is now, minus the last 24 hours
before = now - seconds_in_day

# set where the source of the files are
source = 'C:/Users/kevin/Desktop/Folder A/'

# set the destination path to folder B
destination = 'C:/Users/kevin/Desktop/Folder B/'

def last_mod_time(fname):
    return os.path.getmtime(fname)

    for fname in os.listdir(source):
        src_fname = os.path.join(source, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(destination, fname)
            shutil.move(src_fname, dst_fname)
               
