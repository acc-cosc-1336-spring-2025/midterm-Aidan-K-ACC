import question_b

def question_b_menu():
    print("This program determines if a number is prime or not.\nType 'EXIT' to quit.")
    runstate= "RUN"
    while runstate != "EXIT":
        num= input("Enter a number.\n")
        if num=="EXIT":
            runstate= "EXIT"
            print("Exiting...")
        else:
            print(question_b.is_prime(int(num)))
        

question_b_menu()