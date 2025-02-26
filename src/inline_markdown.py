from textnode import *
import re


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
    new_nodes = []
    for node in old_nodes:
        urls = extract_markdown_images(node.text)
        if urls == [] or node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text_divided = [node.text]
        for i in range(len(urls)):
            new = text_divided[-1].split(f"![{urls[i][0]}]({urls[i][1]})", 1)
            text_divided.pop()
            text_divided.extend([new[0], None, new[1]])

        j = 0
        for i in range(len(text_divided)):
            if text_divided[i] == "":
                continue
            
            if text_divided[i] == None:
                new_nodes.append(TextNode(
                    urls[j][0],
                    TextType.IMAGES,
                    urls[j][1]
                    ))
                j += 1

            else:
                new_nodes.append(TextNode(text_divided[i], node.text_type))
    
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        urls = extract_markdown_links(node.text)
        if urls == [] or node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        text_divided = [node.text]
        for i in range(len(urls)):
            new = text_divided[-1].split(f"[{urls[i][0]}]({urls[i][1]})", 1)
            text_divided.pop()
            text_divided.extend([new[0], None, new[1]])

        j = 0
        for i in range(len(text_divided)):
            if text_divided[i] == "":
                continue
            
            if text_divided[i] == None:
                new_nodes.append(TextNode(
                    urls[j][0],
                    TextType.LINKS,
                    urls[j][1]
                    ))
                j += 1

            else:
                new_nodes.append(TextNode(text_divided[i], node.text_type))
    
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_links(nodes)
    return nodes
