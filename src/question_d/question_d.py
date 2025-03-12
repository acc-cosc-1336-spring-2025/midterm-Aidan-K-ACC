#write functions here, don't add input('') statements here!
def reverse_string(string):
    revstring= ""
    for char in string:
        revstring= str(char)+revstring
    return revstring

