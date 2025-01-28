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
