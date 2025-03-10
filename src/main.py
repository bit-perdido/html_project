from textnode import *
import shutil
import os
from generate_page import generate_pages_recursive
from copystatic import restart_public
import sys


def main():
    
    print("Here len: ", len(sys.argv))
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    base = "./content"
    template = "./template.html"
    to = "./docs"

    restart_public(to)
    
    print("Generating page...")
    generate_pages_recursive(base, template, to, basepath)
         

if __name__ == "__main__":
    main()

