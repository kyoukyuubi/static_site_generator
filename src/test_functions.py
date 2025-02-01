from textnode import *
from htmlnode import *
from functions import *
from inline_markdown import *
from block_markdown import *
import unittest

class TestMain(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """# Header one

This is a paragraph with some *italic* and **bold** text.

* List item 1
* List item 2
* List item 3

1. Ordered item 1
2. Ordered item 2
3. Ordered item 3

> This is a block quote
> with multiple lines

```python
def hello_world():
    print("Hello World!")
```
"""

        expected = ParentNode("div", [
            ParentNode("h1", [
                LeafNode(None, "Header one", None)
            ]),
            ParentNode("p", [
                LeafNode(None, "This is a paragraph with some ", None),
                LeafNode("i", "italic", None),
                LeafNode(None, " and ", None),
                LeafNode("b", "bold", None),
                LeafNode(None, " text.", None)
            ]),
            ParentNode("ul", [
                ParentNode("li", [LeafNode(None, "List item 1", None)]),
                ParentNode("li", [LeafNode(None, "List item 2", None)]),
                ParentNode("li", [LeafNode(None, "List item 3", None)])
            ]),
            ParentNode("ol", [
                ParentNode("li", [LeafNode(None, "Ordered item 1", None)]),
                ParentNode("li", [LeafNode(None, "Ordered item 2", None)]),
                ParentNode("li", [LeafNode(None, "Ordered item 3", None)])
            ]),
            ParentNode("blockquote", [
                LeafNode(None, "This is a block quote\nwith multiple lines", None)
            ]),
            ParentNode("pre", [
                ParentNode("code", [
                    LeafNode(None, "def hello_world():\n    print(\"Hello World!\")", None)
                ])
            ])
        ])
        self.assertEqual(markdown_to_html_node(markdown), expected)