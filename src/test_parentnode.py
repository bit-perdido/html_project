import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_values(self):
        node = ParentNode(
        "p",
        [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ],
        {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertNotEqual(
            node.children,
            []
        )
        self.assertEqual(
            node.value,
            None
        )
        self.assertEqual(
            node.props,
            {"class": "greeting", "href": "https://boot.dev"}
        )
    
    def test_to_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
        ],
        {"class": "greeting", "href": "https://boot.dev"}
        )
        self.assertEqual(
            node.to_html(),
            '<p class="greeting" href="https://boot.dev"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_to_html2(self):
        node = ParentNode(
            "p",
            [LeafNode("b", "Bold text")]
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b></p>"
        )
    
    def test_to_html3(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                ParentNode("n",[
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                    ]),
                LeafNode("b", "Bold text")
            ])
        
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<n><i>italic text</i>Normal text</n><b>Bold text</b></p>"
        )


if __name__ == "__main__":
    unittest.main()
