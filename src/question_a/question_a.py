#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_person_category(age):
    if age<0 or age>125:
        print("invalid number")
    else:
        if age<=1:
            return "infant"
        if age>1 and age<13:
            return "child"
        if age>=13 and age<20:
            return "teenager"
        if age>=20:
            return "adult"

