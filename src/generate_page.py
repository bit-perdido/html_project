from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType
import os
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            almohadillas, text = block.split(" ", 1)
            text = text.replace("\n"," ").strip()
            count = len(almohadillas)
            if count == 1:
                return text
    
    raise Exception("Heading 1 not found")
                

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.isfile(from_path):
        return Exception("No markdown given")
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    template_file = open(template_path, "r")
    template = template_file.read()
    
    html_node = markdown_to_html_node(markdown)
    html_text = html_node.to_html()
    title = extract_title(markdown)
    
    new_page = template.replace("{{ Title }}", title, 1).replace("{{ Content }}", html_text, 1)
    file_name = f"{dest_path}/index.html"
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    new_page_file = open(file_name, "w")
    new_page_file.write(new_page)

