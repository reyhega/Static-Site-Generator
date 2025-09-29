import os
from markdown_blocks import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
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




