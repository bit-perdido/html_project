from textnode import *

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

main()
