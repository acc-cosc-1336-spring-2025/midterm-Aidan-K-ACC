def get_age():
    age= float(input("Please Enter Your Age.\n"))
    return age

def eval_age(age):
    if age<0 or age>125:
        print("invalid number")
    else:
        if age<=1:
            print("infant")
        if age>1 and age<13:
            print("child")
        if age>=13 and age<20:
            print("teenager")
        if age>=20:
            print("adult")

