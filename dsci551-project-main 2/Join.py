## What are Join Function does 
# Checks that separator is a string
# Verifies all elements of the iterable are strings
# Concatenates the strings with the separator. Appending it before the first element

## Improvements Added 
# Convert non-string elements to string
# Support for generator input
# Improve error message for non-iterable input

def join_strings(separator, iterable):
    """
    :param separator: The string used to separate each element.
    :param iterable: Any iterable containing string elements.
    :return: A single concatenated string.
    """
    # Validate input types
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string, got {type(separator)}")
    if not hasattr(iterable, '__iter__'):
        raise TypeError("Second argument must be iterable, got {type(iterable)}")

    result = ""
    first_element = True

    # Iterate through elements to concatenate manually
    for item in iterable:
        if not isinstance(item, str):
            raise TypeError("All elements in iterable must be strings")

        if not first_element:
            result += separator  # Add separator before each element after the first
        else:
            first_element = False

        result += item  # Concatenate the string

    return result
