import unittest
from htmlnode import *

class TestTextNode(unittest.TestCase):
    #Testing HTMLNode
    def test_html_node(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        htmlnode = HTMLNode(tag = "tag text", value = "Value text", props = props)
        excepted = "HTMLNode(tag text, Value text, children: None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(repr(htmlnode), excepted)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_html_props_multi(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        htmlnode = HTMLNode(props=props)
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(htmlnode.props_to_html(), expected)

    def test_html_props_singular(self):
        props = {
            "href": "https://www.google.com",
        }
        htmlnode = HTMLNode(props=props)
        expected = ' href="https://www.google.com"'
        self.assertEqual(htmlnode.props_to_html(), expected)

    def test_ht_html_on_base_class(self):
        htmlnode = HTMLNode("tag text", "Value text")
        with self.assertRaises(NotImplementedError):
            htmlnode.to_html()

    #Testing LeafNode
    def test_leaf_node(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "LeafNode(p, This is a paragraph of text., None)"
        self.assertEqual(repr(node), expected)

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_without_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_value_none(self):
        node = LeafNode("p", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_tag_none(self):
        node = LeafNode("", "this is a string")
        expected = "this is a string"
        self.assertEqual(node.to_html(), expected)

    #Testing ParentNode
    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        excepted = "ParentNode(p, children: [LeafNode(b, Bold text, None), LeafNode(None, Normal text, None), LeafNode(i, italic text, None), LeafNode(None, Normal text, None)], None)" 
        self.assertEqual(repr(node), excepted)

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        excepted = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>" 
        self.assertEqual(node.to_html(), excepted)

    def test_to_html_none_tag(self):
        node = ParentNode(
            "",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_none_children(self):
        node = ParentNode(
            "p",
            [],
        )
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()