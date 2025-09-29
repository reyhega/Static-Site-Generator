import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path, basepath):
    list_content = os.listdir(dir_path_content)
    print(f"'{dir_path_content}' contents: {list_content}")

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursively(from_path, template_path, dest_path, basepath)



def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'...")
    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()
    
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src=/"{basepath}')


    dest_dir = os.path.dirname(dest_path)

    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    
    to_file = open(dest_path, "w")
    to_file.write(template)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line.split("# ", maxsplit=1)[1].strip()
            return title
        
    raise Exception("Missing title")




