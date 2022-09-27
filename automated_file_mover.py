import sys
import os
import shutil
import time

from tkinter import filedialog


dir_names = ['Music', 'Videos', 'Photos']

def creating_directory(path):
    os.chdir(path)
    full_path = path + r'\Sorted Files'
    try:
        os.mkdir(full_path)
        print(f"Successfully created directory at {full_path}")
        for dir_name in dir_names:
            os.mkdir(full_path + f'\\{dir_name}')
            print(f"Successfully created sub directories")
    except OSError:
        print("Couldn't find proper path!")


def loading_files(in_path, out_path):
    os.chdir(in_path)
    while True:
        time.sleep(1)
        files = os.listdir(in_path)
        for file in files:
            if file.endswith('.mp4') or file.endswith('.mpeg'):
                shutil.move(file, out_path + f'\\{dir_names[0]}')
                print(f"Succesfully moved {file} to {dir_names[0]}")
            elif file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                shutil.move(file, out_path + f'\\{dir_names[2]}')
                print(f"Succesfully moved {file} to {dir_names[2]}")

if __name__ == '__main__':
    print("Press any key to select folder where automated files should be sorted...")
    desktop_path = filedialog.askdirectory()
    creating_directory(desktop_path)
    sorted_dir = desktop_path + r'\Sorted Files'
    print("Press any key to select folder where automated files should be downloaded...")
    download_files = filedialog.askdirectory()
    loading_files(download_files, sorted_dir)
