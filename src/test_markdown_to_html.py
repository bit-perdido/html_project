import unittest
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_heading(self):
        md = """
#### This is **bolded** heading
text in a h
tag here

# This is another heading with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>This is <b>bolded</b> heading text in a h tag here</h4><h1>This is another heading with <i>italic</i> text and <code>code</code> here</h1></div>",
    )

    def test_code(self):
        md = """
        
```This is **bolded** code
text in a code
tag here```

```This is another code with _italic_ text and `code` here```
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is **bolded** code text in a code tag here</code></pre><pre><code>This is another code with _italic_ text and `code` here</code></pre></div>"
            )

    def test_quote(self):
        md = """
> This is **bolded** quote
> text in a quote
> tag here

> This is another quote with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> quote text in a quote tag here</blockquote><blockquote>This is another quote with <i>italic</i> text and <code>code</code> here</blockquote></div>"
        )

    def test_list(self):
        md = """
1. This is **bolded** olist
2. text in a quote
3. tag here

- This is another list 
- with _italic_ text and `code` here
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is <b>bolded</b> olist</li><li>text in a quote</li><li>tag here</li></ol><ul><li>This is another list</li><li>with <i>italic</i> text and <code>code</code> here</li></ul></div>"
        )

if __name__ == "__main__":
    unittest.main()