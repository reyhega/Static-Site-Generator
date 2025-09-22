import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()