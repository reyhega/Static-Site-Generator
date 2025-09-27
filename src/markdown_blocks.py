from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")
    
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")
    headings = ("# ", "## ", "### ", "#### ", "##### ", "###### ")

    # Heading
    if block.startswith(headings):
        return BlockType.HEADING
    
    # Code
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    
    # Quote
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    # Unordered List
    if (block.startswith("- ") or block.startswith("* ")):
        for line in lines:
            if not (line.startswith("* ") or line.startswith("- ")):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    
    # Ordered List
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    
    # Paragraph
    return BlockType.PARAGRAPH





