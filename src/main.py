from textnode import *
import shutil
import os


def main():
    restart_public()
         

def restart_public():
    public_path = "/home/reinforced_bread/workspace/bootdev/html_project/root/public"
    static_path = "/home/reinforced_bread/workspace/bootdev/html_project/root/static"
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir("/home/reinforced_bread/workspace/bootdev/html_project/root/public")

    if not os.path.exists(static_path):
        raise ValueError("path for static doesnt exist")
    
    static_contents = os.listdir(static_path)
    
    file_transfer(static_path, public_path)


def file_transfer(source, destination):
    files = []
    dir = []
    source_contents = os.listdir(source)
    for object in source_contents:
        object_path = f"{source}/{object}"
        if os.path.isfile(object_path):
            files.append(object_path)
        else:
            dir.append(object)
    
    if files:
        if not os.path.exists(destination):
            os.mkdir(destination)
        for file in files:
            shutil.copy(file, destination)
    
    if dir:
        for folder in dir:
            folder_source = f"{source}/{folder}"
            folder_destination = f"{destination}/{folder}"
            file_transfer(folder_source, folder_destination)

if __name__ == "__main__":
    main()

