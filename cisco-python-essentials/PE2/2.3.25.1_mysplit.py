def mysplit(string):
    # Clean and copy string into a new variable
    new_string = string.lstrip()
    # Create a list to store its elements
    elements = list()
    # Set the character to look for
    character = ' '

    if not character in string:
        # If not found then return empty list
        return elements
    else:
        # Find the first character
        location = new_string.find(character)
        while location != -1:
            # If found, mark the split
            new_split = location + 1
            # Select element
            element = new_string[:new_split]
            # Strip element from the string
            new_string = new_string.replace(element, '')
            # Append element into the list
            elements.append(element.rstrip())
            # Locate next element
            location = new_string.find(character)
        else:
            # If new_string is not empty (has any remainder)
            if new_string:
                # Append new string remainder into the list
                elements.append(new_string)
                # Strip element from the string
                new_string = new_string.replace(element, '')
        return elements

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
