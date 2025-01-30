from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *

def main():
    text = "# This is a heading"
    print(block_to_block_type(text))

main()