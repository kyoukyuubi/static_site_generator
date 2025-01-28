import unittest
from htmlnode import *

class TestTextNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()