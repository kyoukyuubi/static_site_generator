def markdown_to_blocks(markdown):
    return_list = []
    blocks = markdown.split("\n\n")
    for block in blocks:  
        cleaned = block.strip()
        if cleaned: 
            return_list.append(cleaned)
    return return_list

def block_to_block_type(text):
    #Match the first letter in a string
    match text[0]:
        case "#":
            #Split text into a list for every whitepsace it finds
            parts = text.split(" ")
            #Gets the length of the first parts (The #s)
            first_part = len(parts[0])
            #If the length is between 1 and 6, return heading. Else return nothing and let it go to default
            if 1 <= first_part <= 6:
                return "heading"
        case "`":
            #Check if the first 3 and the last letters are `
            if text.startswith("`" * 3) and text.endswith("`" * 3):
                return "code"
        case ">":
            #Split text into lines using \n
            lines = text.split("\n")
            #If all lines start with > return quote
            if all(line.startswith(">") for line in lines):
                return "quote"
        case "*" | "-":
            #Split text into lines using \n
            lines = text.split("\n")
            #If the 2nd letter in each line has a white space, return unordered_list
            #This works because we only need the first - or * in the line
            #Double check if it still starts with * or -
            if all(
                line.startswith(("*", "-")) and
                len(line) > 1 and
                line[1] == " "
                for line in lines
                ):
                return "unordered_list"
        case n if n.isdigit():
            #Split the text into lines by using \n
            lines = text.split("\n")

            #Check if the text is longer than 3 letters and the 2nd letter is a . where the 2nd letter is a space and the first letter is a digit
            if all(
                len(line) > 2 and
                line[0].isdigit() and
                line[1] == "." and
                line[2] == " "
                for line in lines
            ):
                #If it is set the start of a counter 
                i = 1
                #Loop through the lines and see if the start letter is equal to i, if it is increase i with 1, if it isn't skip the increase
                for line in lines:
                    if line[0] == f"{i}":
                        i += 1
                #Check if the lentgh of lines + 1 (to avoid 0 index) are equal to i, if it is, it means that every line has the correct increminting number
                if (len(lines) + 1) == i:
                    return "ordered_list"
    #If nothing is returned or found, return paragraph
    return "paragraph"