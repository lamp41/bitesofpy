def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    substring = string[n:]
    result = substring + string[:n]
    return result

print(rotate('hello', -2))