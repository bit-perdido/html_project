import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_dif_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_dif_text(self):
        node = TextNode("Thisa text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_dif_type(self):
        node = TextNode("Thisa text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

class TestTextNodeTOHTMLNode(unittest.TestCase):
    def test_normal(self): 
        node = text_node_to_html_node(TextNode("This is a text node", TextType.NORMAL))
        result = LeafNode(None, "This is a text node")
        self.assertEqual(node.value, result.value)
        self.assertEqual(node.tag, result.tag)
        self.assertEqual(node.props, result.props)
    
    def test_bold(self): 
        node = text_node_to_html_node(TextNode("This is a text node", TextType.BOLD))
        result = LeafNode("b", "This is a text node")
        self.assertEqual(node.value, result.value)
        self.assertEqual(node.tag, result.tag)
        self.assertEqual(node.props, result.props)

    def test_italic(self): 
        node = text_node_to_html_node(TextNode("This is a text node", TextType.ITALIC))
        result = LeafNode("i", "This is a text node")
        self.assertEqual(node.value, result.value)
        self.assertEqual(node.tag, result.tag)
        self.assertEqual(node.props, result.props)

    def test_code(self): 
        node = text_node_to_html_node(TextNode("This is a text node", TextType.CODE))
        result = LeafNode("code", "This is a text node")
        self.assertEqual(node.value, result.value)
        self.assertEqual(node.tag, result.tag)
        self.assertEqual(node.props, result.props)

    def test_link(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.LINKS, "https://www.boot.dev"))
        result = LeafNode("a", "This is a text node", {"href":"https://www.boot.dev"})
        self.assertEqual(node.value, result.value)
        self.assertEqual(node.tag, result.tag)
        self.assertEqual(node.props, result.props)

    def test_image(self):
        node = text_node_to_html_node(TextNode("This is a text node", TextType.IMAGES, "https://www.boot.dev"))
        result = LeafNode("img", None, {"src":"https://www.boot.dev", "alt":"This is a text node"})
        self.assertEqual(node.value, result.value)
        self.assertEqual(node.tag, result.tag)
        self.assertEqual(node.props, result.props)


if __name__ == "__main__":
    unittest.main()
