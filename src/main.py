

import os, shutil

from copystatic import copy_files_recursive
from generate_webpage import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_markdown = "./content"
dir_path_template = "./template.html"
dir_path_html = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    
    print("Generating Pages...")
    generate_pages_recursive(dir_path_markdown, dir_path_template, dir_path_html)

if __name__ == "__main__":
    print("Executing main.py")
    main()