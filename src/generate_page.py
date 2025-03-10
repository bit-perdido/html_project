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
    
    raise ValueError("Heading 1 not found")
                

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.isfile(from_path):
        return ValueError("No markdown given")
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()
    
    html_node = markdown_to_html_node(markdown)
    html_text = html_node.to_html()
    title = extract_title(markdown)
    
    new_page = template.replace("{{ Title }}", title, 1).replace("{{ Content }}", html_text, 1)
    new_page = new_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    file_name = f"{dest_path}/index.html"
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    new_page_file = open(file_name, "w")
    new_page_file.write(new_page)
    new_page_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    objects = os.listdir(dir_path_content)
    for object in objects:
        object_path = f"{dir_path_content}/{object}"
        if os.path.isfile(object_path):
            generate_page(object_path, template_path, dest_dir_path, basepath)
        
        elif os.path.isdir(object_path):
            dir_path_object = f"{dir_path_content}/{object}"
            dest_path_object = f"{dest_dir_path}/{object}"
            generate_pages_recursive(dir_path_object, template_path, dest_path_object, basepath)
