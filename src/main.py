import sys


from copy_to_directory import copy_contents_to_directory
from generate_page import generate_pages_recursively

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_docs = "./docs"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]


    copy_contents_to_directory(dir_path_static, dir_path_docs)

    generate_pages_recursively(dir_path_content, template_path, dir_path_docs, basepath)


main ()