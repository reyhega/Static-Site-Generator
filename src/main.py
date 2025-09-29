import os

from copy_to_directory import copy_contents_to_directory
from generate_page import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

from_path = os.path.join(dir_path_content, "index.md")
dest_path = os.path.join(dir_path_public, "index.html")


def main():
    copy_contents_to_directory(dir_path_static, dir_path_public)


    generate_page(from_path, template_path, dest_path)


main ()