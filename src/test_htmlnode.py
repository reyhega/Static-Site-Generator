import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_multiple_props(self):
        node = HTMLNode("a", "Testing multiple props", None, {"href": "https://www.boot.dev", "target": "_self"})
        node_result = ' href="https://www.boot.dev" target="_self"'
        self.assertEqual(node.props_to_html(), node_result)

    def test_single_prop(self):
        node = HTMLNode("img", None, None, {"src": "single_prop.jpg"})
        node_result = ' src="single_prop.jpg"'
        self.assertEqual(node.props_to_html(), node_result)

    def test_empty_props(self):
        node = HTMLNode("p", "Empty props test", None, None)
        node_result = ""
        self.assertEqual(node.props_to_html(), node_result)

    def test_values(self):
        node = HTMLNode("div", "Test, test",)
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Test, test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("p", "This should display...", None, {"class": "deez"})
        self.assertEqual(node.__repr__(),"HTMLNode(tag=p, value=This should display..., children=None, props={'class': 'deez'})")


if __name__ == "__main__":
    unittest.main()