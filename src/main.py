import sys


from copy_to_directory import copy_contents_to_directory
from generate_page import generate_pages_recursively

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_docs = "./docs"
template_path = "./template.html"


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    copy_contents_to_directory(dir_path_static, dir_path_docs)

    generate_pages_recursively(dir_path_content, template_path, dir_path_docs, basepath)


main ()