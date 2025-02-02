from textnode import *
from htmlnode import *
from inline_markdown import *
from block_markdown import *

def process_list_block(block, is_ordered):
    def strip_list_prefix(line):
        if is_ordered:
            return line[line.find(". ") + 2:]
        else:
            if line.startswith("- "):
                return line[2:]  # Skip exactly "- "
            elif line.startswith("* "):
                return line[2:]  # Skip exactly "* "
            return line
        
    tag = "ol" if is_ordered else "ul"
    parent_node = ParentNode(tag, [])

    lines = block.split("\n")
    for line in lines:
        if not line.strip():
            continue
        line_no_prefix = strip_list_prefix(line)
        if line_no_prefix.strip():
            children = text_to_children(line_no_prefix)
            li_node = ParentNode("li", children)
            parent_node.children.append(li_node)
    return parent_node

def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)

    return html_nodes

def markdown_to_html_node(markdown):
    markdown_list = markdown_to_blocks(markdown)
    result_node = ParentNode("div", [])

    for text in markdown_list:
        type = block_to_block_type(text)
        match type:
            case "paragraph":
                children = text_to_children(text)
                p_node = ParentNode("p", children)
                result_node.children.append(p_node)
            case "heading":
                cleaned_text = text.lstrip("#").lstrip()
                children = text_to_children(cleaned_text)
                headling_level = str(len(text.split(" ")[0]))
                tag = "h" + headling_level
                heading_node = ParentNode(tag, children)
                result_node.children.append(heading_node)
            case "code":
                lines = text.split("\n")[1:-1]
                cleaned_text = "\n".join(lines)
                children = text_to_children(cleaned_text)
                code_node = ParentNode("code", children)
                pre_wrapper = ParentNode("pre", [code_node])
                result_node.children.append(pre_wrapper)
            case "quote":
                lines = text.split("\n")
                cleaned_lines = [line.lstrip(">").strip() for line in lines]
                cleaned_text = "\n".join(cleaned_lines)
                children = text_to_children(cleaned_text)
                quote_node = ParentNode("blockquote", children)
                result_node.children.append(quote_node)
            case "unordered_list":
                ul_node = process_list_block(text, False)
                result_node.children.append(ul_node)
            case "ordered_list":
                ol_node = process_list_block(text, True)
                result_node.children.append(ol_node)
    
    return result_node

def extract_title(markdown):
    #Split the markdown text into lines
    lines = markdown.split("\n")

    for line in lines:
        #Check if line starts with # and only 1 #
        if line.startswith("#") and not line.startswith("##"):
            #return the title without the #
            return line.lstrip("#").strip()
            
    #Raise an exception, cause no h1 was found
    raise Exception("No Title markdown was found!")