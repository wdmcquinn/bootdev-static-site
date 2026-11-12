class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        return_string = ""
        for prop in self.props:
            return_string += f' {prop}="{self.props[prop]}"'
        return return_string

    def __repr__(self):
        return f"HTMLNode:\n tag:{self.tag}\n value:{self.value}\n childres:{self.children}\n props:{self.props} /n ------"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode:\n tag:{self.tag}\n value:{self.value}\n props:{self.props} \n ------"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is required!")
        if self.children is None:
            raise ValueError("Children are required!")
        else:
            final_string = f"<{self.tag}>"
            for child in self.children:
                final_string += child.to_html()
            return f"{final_string}</{self.tag}>"