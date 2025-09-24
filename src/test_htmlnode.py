import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_multiple_props(self):
        node = HTMLNode("a", "Testing multiple props", [], {"href": "https://www.boot.dev", "target": "_self"})
        node_result = ' href="https://www.boot.dev" target="_self"'
        self.assertEqual(node.props_to_html(), node_result)

    def test_single_prop(self):
        node = HTMLNode("img", None, [], {"src": "single_prop.jpg"})
        node_result = ' src="single_prop.jpg"'
        self.assertEqual(node.props_to_html(), node_result)

    def test_empty_props(self):
        node = HTMLNode("p", "Empty props test", [], {})
        node_result = ""
        self.assertEqual(node.props_to_html(), node_result)


if __name__ == "__main__":
    unittest.main()