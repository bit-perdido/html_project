from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    divided = markdown.split("\n")
    result = []
    line = ""
    for div in divided:
        if div == "":
            if line == "":
                continue
            result.append(line)
            line = ""   
        
        if line == "":
            line = div.strip()
        else:
            line = f"{line}\n{div.strip()}"

    return result

def block_to_block_type(block):
    lines = block.split("\n")

    if re.findall(r"^#{1,6} (\w|\d)", block):
        return BlockType.HEADING
    elif re.findall(r"^`{3}", block) and re.findall(r"`{3}$", block):
        return BlockType.CODE
    elif re.findall(r"^>", block):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    elif block.startswith("1. "):
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i + 1}. "):
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH