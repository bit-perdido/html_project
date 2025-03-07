from textnode import *
import shutil
import os
from generate_page import generate_page
from copystatic import restart_public


def main():
    restart_public()
    
    base = "./content/index.md"
    template = "./template.html"
    to = "./public"
    generate_page(base, template, to)
         

if __name__ == "__main__":
    main()

