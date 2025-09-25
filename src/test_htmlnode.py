import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):

################# HTMLNode Tests #################

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

################# LeafNode Tests #################

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click here!</a>')

    def test_leaf_to_html_a_self(self):
        node = LeafNode("a", "Click here!", {"href": "https://www.google.com", "target": "_self"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_self">Click here!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "This is plain text")
        self.assertEqual(node.to_html(), "This is plain text")
    
    def test_leaf_repr(self):
        node = LeafNode("a", "This is a link", {"href": "https://www.google.com", "target": "_self"})
        self.assertEqual(node.__repr__(), "LeafNode(tag=a, value=This is a link, props={'href': 'https://www.google.com', 'target': '_self'})")

################# ParentNode Tests #################

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</p>",
        )
    
    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold Text"),
                LeafNode(None, "Normal Text"),
                LeafNode("i", "Italic Text"),
                LeafNode(None, "Normal Text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold Text</b>Normal Text<i>Italic Text</i>Normal Text</h2>",
        )
    
    def test_to_html_props(self):
        child_node = LeafNode("a", "This is a link", {"href": "https://www.google.com"})
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), '<p><a href="https://www.google.com">This is a link</a></p>')

if __name__ == "__main__":
    unittest.main()