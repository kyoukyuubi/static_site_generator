from textnode import *

def main():
    textnode = TextNode("this is a test string", TextType.TEXT, "https://www.boot.dev")
    othernode = TextNode("Another text node", TextType.TEXT)
    print(textnode == othernode)
    print(textnode)


main()