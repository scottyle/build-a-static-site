from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(
            self,
            text:str,
            text_type:object, #The type of text this node contains, which is a member of the TextType enum
            url:str = None # The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

        ) -> None:

        self.text = text
        self.text_type = text_type
        self.url = url 

    
    def __eq__(self,other:object):
        """
        Compares self to another TextNode instance (other) and returns True if all their properties are equal
        """
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    
    def __repr__(self):
        """
        Returns a string representation of TextNode object 
        """
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"