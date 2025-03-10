import os
import shutil


def restart_public(page_root):
    static_path = "./static"
    if os.path.exists(page_root):
        print(f"Deleting {page_root} directory...")
        shutil.rmtree(page_root)
    else:
        print("Public directory missing, creating new one...")
    os.mkdir(page_root)

    if not os.path.exists(static_path):
        raise ValueError("path for static doesnt exist")
    
    print(f"Copying static files to {page_root} directory...")
    file_transfer(static_path, page_root)


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
            print(f" * {file} -> {destination}")
            shutil.copy(file, destination)
    
    if dir:
        for folder in dir:
            folder_source = f"{source}/{folder}"
            folder_destination = f"{destination}/{folder}"
            file_transfer(folder_source, folder_destination)