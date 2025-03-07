import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_heading(self):
        markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = "This is a heading"
        self.assertEqual(extract_title(markdown), result)

    def test_multiple_headings(self):
        markdown = """
## This is the wrong heading  

#### This is also a wrong heading

# This is a heading

###### This is the last wrong heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        result = "This is a heading"
        self.assertEqual(extract_title(markdown), result)