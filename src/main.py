from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *
from functions import *

def main():
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
    node = markdown_to_html_node(markdown)
    print(node)

main()