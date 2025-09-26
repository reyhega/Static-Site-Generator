import re
from textnode import TextNode, TextType

def text_to_textnodes(text):

    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    old nodes -> list of nodes
    delimiter -> character to separate nodes

    returns a list of split nodes
    '''
    new_nodes = []

    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimiter)

        '''If we have an even number of sections, 
        it means we have an unclosed delimiter (like **bold text without the closing **). 
        Valid markdown should always have pairs of delimiters.'''

        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown syntax, formatted section not closed")
        
        ''' This loops through each section:
        Skips empty sections
        Even-indexed sections (0, 2, 4...) are regular text
        Odd-indexed sections (1, 3, 5...) are the formatted text between delimiters
        '''
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type)) 

        new_nodes.extend(split_nodes)
    
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    images = re.findall(pattern, text)
    return images

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links = re.findall(pattern, text)
    return links
        
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        markdown_imgs = extract_markdown_images(original_text)

        if len(markdown_imgs) == 0:
            new_nodes.append(node)
            continue

        for image in markdown_imgs:
            sections = original_text.split(f"![{image[0]}]({image[1]})")
            if len(sections) != 2:
                raise ValueError("Invalid Markdown, image seciton not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        markdown_links = extract_markdown_links(original_text)

        if len(markdown_links) == 0:
            new_nodes.append(node)
            continue

        for link in markdown_links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown, link seciton not closed")
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes