

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        out = []
        for k in self.props.keys():
            out.append(f'{k}="{self.props[k]}"')
        return " "+" ".join(out)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value=None, props=None):
        children=None
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if self.value==None:
            raise ValueError
        if self.tag==None:
            return self.value
        if self.props==None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        value=None
        super().__init__(tag, value, children, props)
    def to_html(self):
        if self.tag==None:
            raise ValueError("missing tag")
        if self.children==None:
            raise ValueError("missing children")
        li=[]
        for i in self.children:
            li.append(i.to_html())
        return f"<{self.tag}>{"".join(li)}</{self.tag}>"

        
        
        