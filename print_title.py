"""
Filename: print_title.py
Author: Abbi Rath
Created: 2/17/23
Purpose: Print program title function or module
"""


def main():
    print(title("Print Title Test!"))


def title(statement):
    """
        Takes in a string argument
        returns a string with ascii decorations
    """
    # Get the length of the statement
    text_length = len(statement)

    # Create the title string 
    # Initalize the result string variable
    result = ""
    result = result + "+--" + "-" * text_length + "--+\n"
    result = result + "|  " + statement + "  |\n"
    result = result + "+--" + "-" * text_length + "--+\n"

    return result


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()