import re
def get_index_different_char(chars):
    chars_str = ''.join(str(char) for char in chars)
    result = re.findall(r"[a-zA-Z\d]", chars_str)
    print(result)
    if len(result) == 1 :
        if result[0].isdigit():
            char = int(result[0])
        else:
            char = result[0]
        print('alphabetic')
        return chars.index(char)
    else:
        result = re.search(r"[^a-zA-Z\d:]", chars_str).group()
        print(result)
        return chars.index(result[0]) 

print(str(get_index_different_char(['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'])))