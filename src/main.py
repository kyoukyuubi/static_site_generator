import os
import shutil
from functions import extract_title, markdown_to_html_node

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

def generate_page(from_path, template_path, dest_path):
    #Print a msg to show what it is going to do
    #This is a non debug messege!
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #Open the Markdown file
    with open(from_path) as file:
        #Open the file and store it
        md_conents = file.read()

    #Open the html template file
    with open(template_path) as file:
        #Open the file and store it
        template_conents = file.read()

    #Convert markdown to HTMLNode
    node = markdown_to_html_node(md_conents)
    #Store the actual HTML
    html_string = node.to_html()

    #Get the Title from the markdown text
    title = extract_title(md_conents)

    #Modify the template in a new var that has the title and the html_string
    insert_title = template_conents.replace("{{ Title }}", title)
    insert_content = insert_title.replace("{{ Content }}", html_string)

    #Store the path as a correct path name
    path = os.path.dirname(dest_path)

    #Make the dir if it doesn't exsist
    os.makedirs(path, exist_ok=True)

    #Make the file, save and close it
    with open(dest_path, 'w') as file:
        file.write(insert_content)

def main():
    try:
        if copy_recursive("static", "public"):
            print("Operation succeded!")
        generate_page("content/index.md", "template.html", "public/index.html")
    except Exception as e:
        print (f"Execption Caught: {e}")

main()