# Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.
# Do not use built in functions.
# Usage:
# should return 'dGhpcyBpcyBhIHN0cmluZyEh'
# to_base_64('this is a string!!')
# should return 'this is a string!!'
# from_base_64('dGhpcyBpcyBhIHN0cmluZyEh')

def to_base_64(string):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bitstring = ""
    result = ""
    for s in string:
        bitstring += bin(ord(s))[2:].zfill(8)
    if len(bitstring) % 6 != 0:
        bitstring += "0" * (6 - (len(bitstring) % 6))
    for i in range(0, len(bitstring) - 1, 6):
        result += base64[int(bitstring[i:i+6], 2)]
    return result
    
def from_base_64(string):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bitstring = ""
    result = ""
    for s in string:
        bitstring += bin(base64.index(s))[2:].zfill(6)
    for i in range(0, len(bitstring) - 1, 8):
        result += chr(int(bitstring[i:i+8], 2))
    if result.endswith('\x00'):
        result = result[:-1]
    return result
   
