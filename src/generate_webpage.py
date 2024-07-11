import os, shutil

from markdown_blocks import (
    markdown_to_blocks, markdown_to_html_node
)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    header = blocks[0]
    if header.startswith('# '):
        return header.strip('# ')
    
def generate_page(src, template_path, dst):
    print(f"Generating page from {src} to {dst} using {template_path}")
    
    with open(src, mode='r') as f:
        from_data = f.read()

    with open(template_path, mode='r') as f:
        template_data = f.read()

    title = extract_title(from_data)
    top_node = markdown_to_html_node(from_data)

    html = top_node.to_html()

    template_data = template_data.replace("{{ Title }}", title)
    template_data = template_data.replace("{{ Content }}", html)

    with open(dst, mode='w') as f:
        f.write(template_data)

def generate_pages_recursive(src, template_path, dst):
    paths = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)

    for path in paths:
        src_path = os.path.join(src, path)
        dst_path = os.path.join(dst, path)
        
        if os.path.isfile(src_path):
            if src_path[-3:] == '.md':
                generate_page(src_path, template_path, f"{dst_path[:-3]}.html")

        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dst_path)

        
        
