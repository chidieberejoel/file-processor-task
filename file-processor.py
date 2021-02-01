"""
Created on Mon Feb 01, 2020
Complete document analysis:
1) Read and process all files
2) Reverse the order of each line and each character in the file(s)
3) Write output with additional (.reversed) extension
@author: Chidiebere Joel
@email: chidiebereyjoel@gmail.com
"""

#Imports
import os, logging

#Set file extension for specific filetypes
fileext = '.data'
#Set directory of files for processing and reversed files
compdir = input("Enter a directory: ")

#get all of the files in the directory into a list
txt_files = list(filter(lambda x: x.endswith(fileext), os.listdir(compdir)));

# setup default module logging
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def reversed_fp_iter(filename, buf_size=8192):
    """
        reverse the order of each line in the file, and for each character line in the file
    """
    with open(filename) as fp:
        # holds possible incomplete segment at the beginning of the buffer
        segment = None
        offset = 0
        fp.seek(0, os.SEEK_END)
        file_size = remaining_size = fp.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fp.seek(file_size - offset)
            buffer = fp.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.splitlines(True)
            # the first line of the buffer is probably not a complete line so
            # it will be saved and appended to the last line of the next buffer
            if segment is not None:
                # If the previous chunk starts right from the beginning of line
                # do not concat the segment to the last line of new chunk.
                # Instead, yield the segment first 
                if buffer[-1] != '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0][::-1]
            for index in range(len(lines) - 1, 0, -1):
                if len(lines[index]):
                    yield lines[index][::-1]
        # Don't yield None if the file was empty
        if segment is not None:
            yield segment


def save_reversed(files):
    """
        save in new .reversed files
    """
    log.info("Processing files {}...".format(files))
    for file in files:
        # join file name with input directory
        outfile_directory = os.path.join(compdir, file)
        g = reversed_fp_iter(outfile_directory )
        with open(outfile_directory + ".reversed","w") as newfile:
            #read generator output
            for x in g:
                newfile.write(str(x))
    log.info("Processing complete")

save_reversed(txt_files);
