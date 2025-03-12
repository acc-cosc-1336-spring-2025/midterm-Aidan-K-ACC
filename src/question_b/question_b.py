#write functions here, don't add input('') statements here!
def is_prime(num):
    n1= 0
    while n1<num:
        n2= 0
        while n2<num:
            if n1*n2==num:
                return False
            else:
                n2+=1
        n1+=1
    else:
        return True

