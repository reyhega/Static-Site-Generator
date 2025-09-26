import unittest

from inline_markdown import (split_nodes_delimiter, extract_markdown_images, extract_markdown_links)

from textnode import TextNode, TextType

class TestSplitDelimeter(unittest.TestCase):

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        node_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]       
        self.assertEqual(new_nodes, node_result)

    def test_delim_double_bold(self):
        node = TextNode("These should be **bolded words**, and also **this**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        node_result = [
            TextNode("These should be ", TextType.TEXT),
            TextNode("bolded words", TextType.BOLD),
            TextNode(", and also ", TextType.TEXT),
            TextNode("this", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, node_result)
    
    def test_delim_bold_italic(self):
        node = TextNode("This text has **bold words** and _italic words_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        node_result = [
            TextNode("This text has ", TextType.TEXT),
            TextNode("bold words", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic words", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, node_result)

################# ExtractMarkdown Tests #################

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Thisis a text with a [link](https://google.com) and [another link](https://youtube.com)"
        )
        self.assertListEqual(
            [
                ("link", "https://google.com"),
                ("another link", "https://youtube.com"),
            ],
            matches,
        )


if __name__ == "__main__":
    unittest.main()