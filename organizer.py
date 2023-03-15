import os
import shutil
import logging
import sys
   
def remover(rootDir):
    # Command-line argument was provided
    for dirName, subdirList, fileList in os.walk(rootDir):
        # loop through each file
        for fname in fileList:
            # if the file is a certain type, keep it
            if fname.endswith('.mkv') or fname.endswith('.mp4') or fname.endswith('.srt') or fname.endswith('.!qB'):
                continue
            # otherwise, delete it
            os.remove(os.path.join(dirName, fname))
            logging.info('File ' + fname + ' deleted in ' + dirName)
            
def mover(rootDir):
    # Walk through the path
    for root, dirs, files in os.walk(rootDir):
        # loop through each file
        for file in files:
            # if there is a .mkv file
            if file.endswith(".mkv"):
                # go through the sub directories
                for subdir in dirs:
                    # check the directory for a .srt file
                    if os.path.exists(os.path.join(root, subdir, file[:-4] + ".srt")):
                        # move the .srt file out of the subfolder
                        shutil.move(os.path.join(root, subdir, file[:-4] + ".srt"), root)
                        logging.info('Sub file ' + os.path.join(file[:-4] + ".srt") +  ' moved in ' + os.path.join(root, subdir))

def empty(rootDir):
    # Walk through the path
    for root, dirs, files in os.walk(rootDir):
        # walk through subfolders
        for dir in dirs:
            # generate directory path
            full_path = os.path.join(root, dir)
            # if path empty delete folder
            if not os.listdir(full_path):
                shutil.rmtree(full_path)
                logging.info('Empty folder ' + dir + ' deleted in ' + root)

try:
    # get working directory from command line argument
    home = sys.argv[1]
    # Write status to log file
    logging.basicConfig(filename=home+'/organizer.log', level=logging.INFO, format='%(asctime)s %(message)s')
    logging.info('------------------------------ Starting ------------------------------')
    # set /movies as working dir and run
    rootDir = home + '/movies'
    remover(rootDir)
    mover(rootDir)
    empty(rootDir)
    # set /tv as working dir and run
    rootDir = home + '/tv'
    remover(rootDir)
    mover(rootDir)
    empty(rootDir)
except Exception as e:
    logging.exception(e)
    
logging.info('-------------------------------- Done --------------------------------')