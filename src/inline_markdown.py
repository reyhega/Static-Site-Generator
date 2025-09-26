import re
from textnode import TextNode, TextType

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
        
