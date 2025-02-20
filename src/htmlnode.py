class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        line = ""
        if not self.props:
            return line
        for attribute in self.props:
            line = f'{line} {attribute}="{self.props[attribute]}"'
        return line
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode requires a value")
        if not self.tag:
            return self.value 
        return f"<{self.tag}{self.props_to_html()}>{self.value}<{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"