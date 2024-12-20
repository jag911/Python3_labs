import sys
import glob
import os

# Get the directory name.
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern.
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
filenames = glob.glob(pattern)
# TODO: use os.path.getsize to find each file's size
for file in filenames:
    size = os.path.getsize(file)
# TODO: Add a test to only display files that are not zero length
    if size > 0:
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
        print(f"{os.path.basename(file)}: {size}")
