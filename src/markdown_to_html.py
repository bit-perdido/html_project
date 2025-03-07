from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

parts = []
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childs = []
    for block in blocks:
        childs.append(create_html_node(block))
    return ParentNode("div", childs)


def text_to_children(text): 
    children = []
    children_nodes = text_to_textnodes(text)
    for child in children_nodes:
        children.append(text_node_to_html_node(child))
    return children

def create_html_node(block):
    blocktype = block_to_block_type(block)
    match blocktype:
        case BlockType.QUOTE:
            return single_tag_constructor(block, "blockquote")
        case BlockType.CODE:
            return code_tag_constructor(block)
        case BlockType.PARAGRAPH:
            return single_tag_constructor(block, "p")
        case BlockType.ULIST:
            return list_tag_constructor(block, "ul")
        case BlockType.OLIST:
            return list_tag_constructor(block, "ol")
        case BlockType.HEADING:
            return heading_tag_constructor(block)


def single_tag_constructor(block, tag):
    if tag == "blockquote":
        text = block.replace("\n> "," ").removeprefix("> ")
    else:
        text = block.replace("\n"," ")

    return ParentNode(tag, text_to_children(text))

def list_tag_constructor(block, tag):
    if tag == "ul":
        x = 2
    else :
        x = 3
    
    lines = block.split("\n")
    list_items = []
    for line in lines:
        item_nodes = text_to_textnodes(line[x:].replace("\n"," "))
        item_html_list = []
        for item in item_nodes:
            item_html_list.append(text_node_to_html_node(item))
        list_items.append(ParentNode("li", item_html_list))

    return ParentNode(tag, list_items)

def code_tag_constructor(block):
    text = block[3:-3].replace("\n"," ")
    children = text_node_to_html_node(TextNode(text, TextType.CODE))

    return ParentNode("pre", [children])


def heading_tag_constructor(block):
    almohadillas, text = block.split(" ", 1)
    text = text.replace("\n"," ")
    count = len(almohadillas)
    if count > 6:
        raise ValueError("invalid heading count: {count}")
    tag = f"h{count}"

    return ParentNode(tag, text_to_children(text))