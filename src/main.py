import os
import shutil

def copy_recursive(source, destination):
    #Clean the destination if it already exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    #Create the destination directory fresh
    os.mkdir(destination)

    #Store the items in the source dir
    dir_list = os.listdir(source)

    for item in dir_list:
        #Store the full patch of the item
        full_path = os.path.join(source, item)

        #Check if full_path findes a file
        if os.path.isfile(full_path):
            shutil.copy(full_path, destination)
        #Check if full_path findes a subdirectory
        elif os.path.isdir(full_path):
            #Call itself on the subdirectory
            copy_recursive(full_path, os.path.join(destination, item))
    return True

def main():
    try:
        if copy_recursive("static", "public"):
            print("Operation succeded!")
    except Exception as e:
        print (f"Execption Caught: {e}")

main()