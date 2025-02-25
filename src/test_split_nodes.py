import unittest
from inline_markdown import split_nodes_image, split_nodes_links
from textnode import TextType, TextNode

class TestSplitNodesImages(unittest.TestCase):
    def test_image(self):
        old_nodes = [
            TextNode(
                "This is text with a link ![to boot dev](https://www.boot.dev) isn't it pretty",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" isn't it pretty", TextType.NORMAL)
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            results
        )
    
    def test_images(self):
        old_nodes = [
            TextNode(
                "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) isn't it pretty",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
            TextNode(" isn't it pretty", TextType.NORMAL)
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            results
        )
    
    def test_images_at_borders(self):
        old_nodes = [
            TextNode(
                "![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            results
        )
    
    def test_no_image_and_type(self):
        old_nodes = [
            TextNode(
                "This is text with a link and something else",
                TextType.BOLD
                     )
        ]
        results = [
            TextNode("This is text with a link and something else", TextType.BOLD),
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            results
        )
    
    def test_multiple_nodes_images(self):
        old_nodes = [
            TextNode(
                "1This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev) isn't it pretty",
                TextType.NORMAL
                     ),
            TextNode(
                "![2to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("1This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev"),
            TextNode(" isn't it pretty", TextType.NORMAL),
            TextNode("2to boot dev", TextType.IMAGES, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.IMAGES, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(
            split_nodes_image(old_nodes),
            results
        )


class TestSplitNodesLinks(unittest.TestCase):
    def test_link(self):
        old_nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) isn't it pretty",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" isn't it pretty", TextType.NORMAL)
        ]
        self.assertEqual(
            split_nodes_links(old_nodes),
            results
        )
    
    def test_links(self):
        old_nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) isn't it pretty",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
            TextNode(" isn't it pretty", TextType.NORMAL)
        ]
        self.assertEqual(
            split_nodes_links(old_nodes),
            results
        )
    
    def test_links_at_borders(self):
        old_nodes = [
            TextNode(
                "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(
            split_nodes_links(old_nodes),
            results
        )
    
    def test_no_link(self):
        old_nodes = [
            TextNode(
                "This is text with a link and something else",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("This is text with a link and something else", TextType.NORMAL),
        ]
        self.assertEqual(
            split_nodes_links(old_nodes),
            results
        )

    def test_multiple_nodes_links(self):
        old_nodes = [
            TextNode(
                "1This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) isn't it pretty",
                TextType.NORMAL
                     ),
            TextNode(
                "[2to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                TextType.NORMAL
                     )
        ]
        results = [
            TextNode("1This is text with a link ", TextType.NORMAL),
            TextNode("to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev"),
            TextNode(" isn't it pretty", TextType.NORMAL),
            TextNode("2to boot dev", TextType.LINKS, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("to youtube", TextType.LINKS, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(
            split_nodes_links(old_nodes),
            results
        )

    

if __name__ == "__main__":
    unittest.main()