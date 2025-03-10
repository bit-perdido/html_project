from markdown_to_html import *


def main():
    md = """
![JRR Tolkien sitting](/images/tolkien.png)
"""

    node = markdown_to_html_node(md)
    print(node)
    html = node.to_html()
    
        

if __name__ == "__main__":
    main()