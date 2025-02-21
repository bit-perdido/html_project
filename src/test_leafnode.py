import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_values(self):
        node = LeafNode(
            "bold",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.tag,
            "bold"
        )
        self.assertEqual(
            node.value,
            "Hello, world!"
        )
        self.assertEqual(
            node.props,
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.children,
            None
        )
    
    def test_to_html(self):
        node = LeafNode(
            "bold",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            '<bold class="greeting" href="https://boot.dev">Hello, world!</bold>',
            node.to_html()
        )
    
    def test_to_html_no_tag(self):
        node = LeafNode(
            None,
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.value,
            node.to_html()
        )
    
    def test_repr(self):
        node = LeafNode(
            "bold",
            "Hello, world!",
            {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.__repr__(),
            "LeafNode(bold, Hello, world!, {'class': 'greeting', 'href': 'https://boot.dev'})"
        )

if __name__ == "__main__":
    unittest.main()