from textnode import TextNode, TextType

test=TextNode("This is some anchor text",text_type=TextType.LINK,url="https://www.boot.dev")
print(test)