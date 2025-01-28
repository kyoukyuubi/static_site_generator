class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented in base class")
    
    def props_to_html(self):
        #Check if self.props is None
        if self.props == None:
            return ""
        
        #Make an empty string and loop over self.props adding key=value to the string, with a space in the start
        html_string = ""
        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        return html_string
    
    def __repr__(self):
        #Return the values of the class as a string for debugging purposes
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    #Construct the LeafNode, but we set children to None, since children isn't allowed in a LeafNode
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        #Check if value is None or "" and raise a ValueError if so
        if self.value == None or self.value == "":
            raise ValueError("All leaf nodes must have a value")
        #Check if tag is None or "", return value if so
        if self.tag == None or self.tag == "":
            return f"{self.value}"
        #If tag and value is not None and "", the return the tag and value as a html string. It includes the props, which is why we call the function
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        #Return the values of the class as a string for debugging purposes
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    #Construct the ParentNode, we set value to None since value isn't allowed in a ParentNode, it only handles the children.
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        #Check to see if tag is None or "" and raise an error if so, since tag is required
        if self.tag == None or self.tag == "":
            raise ValueError("Tag cannot be None or an empty string")
        #Check to see if children is None or "" and raise en error if so, since they are required
        if self.children == None or self.children == [] or not isinstance(self.children ,list):
            raise ValueError("Children cannot be None or empty string or list")
        
        #Set an empty string, and loop through the children, calling their function .to_html seperately and add the result to the string, then return it.
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        #Return the values of the class as a string for debugging purposes
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"