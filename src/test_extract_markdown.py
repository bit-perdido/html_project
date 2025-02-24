from main import extract_markdown_images, extract_markdown_links
import unittest

class TestExtractMarkdownImages(unittest.TestCase):
    def test_link_alone(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_images(text),
            [tuple(["rick roll", "https://i.imgur.com/aKaOqIh.gif"])]
        )

    def test_multiple_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            [
                tuple(["rick roll", "https://i.imgur.com/aKaOqIh.gif"]),
                tuple(["obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"])
            ]
        )

    def test_no_image_exclamation(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_images(text),
            []
        )

    def test_various_broken_images(self):
        text = "This is ![hithere] text wi!(das)th a ![rick roll(https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg"
        self.assertEqual(
            extract_markdown_images(text),
            []
        )

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_link_alone(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(
            extract_markdown_links(text),
            [tuple(["rick roll", "https://i.imgur.com/aKaOqIh.gif"])]
        )

    def test_multiple_links(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_links(text),
            [
                tuple(["rick roll", "https://i.imgur.com/aKaOqIh.gif"]),
                tuple(["obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"])
            ]
        )
    
    def test_link_exclamation(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            extract_markdown_links(text),
            []
        )
    
    def test_various_broken_links(self):
        text = "This is [hithere] text wi(das)th a [rick roll(https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg"
        self.assertEqual(
            extract_markdown_links(text),
            []
        )