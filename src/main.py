from textnode import *
from htmlnode import *

def main():
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    htmlnode = HTMLNode("tag text", "Value text", None, props)
    to_html = htmlnode.props_to_html()
    print(htmlnode)
    print(f"String:{to_html}")

main()