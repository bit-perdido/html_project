import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1, node2)
    
    def test_props_to_html(self):
        prop1 = {
            "1": "asdasd",
            "2": "dasdsa"
         }
        node1 = HTMLNode(None, None, None, prop1)
        expected_result =  ' 1="asdasd" 2="dasdsa"'
        self.assertEqual(expected_result, node1.props_to_html())

    def test_eq_2(self):
        node1 = HTMLNode("Lorem Ipsum", None, 3)
        node2 = HTMLNode("Lorem Ipsum", None, 3)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()