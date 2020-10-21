import os
from zipfile import ZipFile

def zip_me(path):
    folder_name = path.split("\\")[-1]
    rel_path = path.strip(folder_name)
    os.chdir(rel_path)

    parse = ZipFile(f"{folder_name}.zip", "w")

    for root, dirs, files in os.walk(folder_name, topdown=False):
        for name in files:
            file = os.path.join(root, name)
            parse.write(file)
            
        for name in dirs:
            folders = os.path.join(root, name)
            parse.write(folders)

    parse.close()

if __name__ == "__main__":
    path = input(r"Path to target folder: ")
    zip_me(path)