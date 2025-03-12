#write functions here, don't add input('') statements here!
def get_sum_of_evens(num):
    total= 0
    for n in (range(0,(num+1))):
        if n%2==0:
            total+= n
    return total

