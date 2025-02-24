from textnode import *
import re

def main():
    first = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(first)     

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL or delimiter not in node.text:
            new_nodes.append(node)
         
        else:
            divided_text = node.text.split(delimiter)
            if len(divided_text) % 2 == 0:
                raise ValueError("invalud Markdown syntax, formatted section not closed")
            new_node = []
            for i in range(len(divided_text)):
                if divided_text[i] == "":
                    continue
                if i % 2 == 0:
                    new_node.append(TextNode(divided_text[i], TextType.NORMAL))
                else:
                    new_node.append(TextNode(divided_text[i], text_type))
            new_nodes.extend(new_node)

    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[.+?\]\(.+?\)", text)
    images_ordered = []
    for image in images:
        info = re.findall(r"\[.+?\]|\(.+?\)", image)
        for i in range(2):
            info[i] = info[i][1:-1]
        images_ordered.append(tuple(info))
    
    return images_ordered

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[.+?\]\(.+?\)", text)
    links_ordered = []
    for link in links:
        info = re.findall(r"\[.+?\]|\(.+?\)", link)
        for i in range(2):
            info[i] = info[i][1:-1]
        links_ordered.append(tuple(info))
    
    return links_ordered

def split_nodes_image(old_nodes):
    pass

main()
