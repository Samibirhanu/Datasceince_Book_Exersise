# We can make strings with single and double quatation marks
single_quoted_string = 'data science'
double_quoted_string = "data science"

# Python uses backslashed '\'  to encode special characters.
tab_string = "\t"   # represents the tab character
print(len(tab_string))     # is 1

# Backslashes as backslashes use raw strings using r""
not_tab_string = r"\t"        # represent the characters '\' 't'
print(len(not_tab_string))    # is 2 

# Create multiline strings using three double quotes.
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
print(multi_line_string)

# String concatnation
first_name = "Samuel"
last_name = "Birhanu"

full_name = first_name + " " + last_name              # string addition
print(full_name)

full_name2 = "{0} {1}".format(first_name, last_name)  #string.format
print(full_name2)

# concatnation wit f-string

full_name3 = f"{first_name} {last_name}"
print(full_name3)