from textnode import *
from htmlnode import *
from text_tools import *
from markdown_blocks import *

def main():
    t_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(t_node)

    h_node = HTMLNode(tag="<b>", value="stuff to test here", children=["h1", "p"], props={"href": "https://boot.dev", "target": "_blank"})
    print (h_node)

    l_node = LeafNode(tag="a", value="click me!", props={"href": "https://boot.dev"})
    print(l_node)

    md = '''
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
'''

    md2 = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
    print(markdown_to_blocks(md2))
main()