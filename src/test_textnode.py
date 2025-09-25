import unittest

from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_1(self):
        node = TextNode("This is an image", TextType.IMAGE, "linktoimage.png")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is an image", TextType.IMAGE, "linktoimage.png")
        node2 = TextNode("This is a link", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node, node2)


class TextTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_img(self):
        node = TextNode("this is an image", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com", "alt": "this is an image"},
        )

    def test_link(self):
        node = TextNode("this is a link", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is a link")
        self.assertEqual(
            html_node.props,
            {"href": "https://www.google.com"},
        
        )


if __name__ == "__main__":
    unittest.main()