import unittest
from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
            #For the text, make sure the text is all the way to the left, else it takes it as a gaint space!
            text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

            expected = [
        '# This is a heading',
        'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
        '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
    ]
            self.assertEqual(expected, markdown_to_blocks(text))

    def test_block_to_block_type(self):
        text_headline = "## headline"
        text_error_headline = "####### headline"
        text_error_headline1 = "###headline"
        text_code = """```
        code text here
        ```"""
        text_quote = """>Code
>More code
>Final code?
>Just kidding!"""
        text_unordered_list = """* list item
* list item
* list item"""
        text_unordered_list1 = """- list item
- list item
- list item"""
        text_ordered_list = """1. Line 
2. Line 
3. Line 
4. Line"""
        text_error_ordered_list = """1. Line 
2. Line 
4. Line 
3. Line""" 
        text_error_unordered_list = """list item
- list item
- list item"""
        text_paragraph = "This is a paragraph!"

        self.assertEqual(block_to_block_type(text_headline), "heading")
        self.assertEqual(block_to_block_type(text_error_headline), "paragraph")
        self.assertEqual(block_to_block_type(text_error_headline1), "paragraph")
        self.assertEqual(block_to_block_type(text_code), "code")
        self.assertEqual(block_to_block_type(text_quote), "quote")
        self.assertEqual(block_to_block_type(text_unordered_list), "unordered_list")
        self.assertEqual(block_to_block_type(text_unordered_list1), "unordered_list")
        self.assertEqual(block_to_block_type(text_ordered_list), "ordered_list")
        self.assertEqual(block_to_block_type(text_paragraph), "paragraph")
        self.assertEqual(block_to_block_type(text_error_unordered_list), "paragraph")
        self.assertEqual(block_to_block_type(text_error_ordered_list), "paragraph")