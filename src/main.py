from textnode import *
from htmlnode import *
def main():
    t_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(t_node)

    h_node = HTMLNode(tag="<b>", value="stuff to test here", children=["h1", "p"], props={"href": "https://boot.dev", "target": "_blank"})
    print (h_node)

    l_node = LeafNode(tag="a", value="click me!", props={"href": "https://boot.dev"})
    print(l_node)

main()