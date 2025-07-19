import os


def list_files_by_extension(folder_path):
    items = os.listdir(folder_path)
    for name in items:
        print(name)
