from textnode import *
import shutil
import os
from generate_page import generate_pages_recursive
from copystatic import restart_public


def main():
    restart_public()
    
    base = "./content"
    template = "./template.html"
    to = "./public"
    print("Generating page...")
    generate_pages_recursive(base, template, to)
         

if __name__ == "__main__":
    main()

