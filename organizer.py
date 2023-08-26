import os
import shutil
import logging
import sys
import datetime

def clear_log(log_file_path):
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=30)

    with open(log_file_path, "r") as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if line.startswith("[")]
    filtered_lines = [line for line in filtered_lines if datetime.datetime.strptime(line.split(']')[0][1:], '%Y-%m-%d %H:%M:%S,%f') >= cutoff_date]

    with open(log_file_path, "w") as file:
        file.writelines(filtered_lines)
        
def remover(root_dir):
    # Command-line argument was provided
    for dir_name, subdir_list, file_list in os.walk(root_dir):
        # loop through each file
        for fname in file_list:
            # if the file is a certain type, keep it
            if fname.endswith('.mkv') or fname.endswith('.mp4') or fname.endswith('.srt') or fname.endswith('.!qB'):
                continue
            # otherwise, delete it
            os.remove(os.path.join(dir_name, fname))
            logging.info('File ' + fname + ' deleted in ' + dir_name)
            
def mover(root_dir):
    # Walk through the path
    for root, dirs, files in os.walk(root_dir):
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

def empty(root_dir):
    # Walk through the path
    for root, dirs, files in os.walk(root_dir):
        # walk through subfolders
        for dir in dirs:
            # generate directory path
            full_path = os.path.join(root, dir)
            # if path empty delete folder
            if not os.listdir(full_path):
                shutil.rmtree(full_path)
                logging.info('Empty folder ' + dir + ' deleted in ' + root)

if __name__ == "__main__":
    try:
        # get working directory from command line argument
        home = sys.argv[1]
        # Write status to log file
        logging.basicConfig(filename=home+'/organizer.log', level=logging.INFO, format='[%(asctime)s] - %(levelname)s: %(message)s')
        logging.info('------------------------------ Starting ------------------------------')
        # set /movies as working dir and run
        root_dir = home + '/movies'
        remover(root_dir)
        mover(root_dir)
        empty(root_dir)
        # set /tv as working dir and run
        root_dir = home + '/tv'
        remover(root_dir)
        mover(root_dir)
        empty(root_dir)
        # clear 30 day old log entries
        clear_log(home+'/organizer.log')
    except Exception as e:
        logging.exception(e)
        
    logging.info('-------------------------------- Done --------------------------------')