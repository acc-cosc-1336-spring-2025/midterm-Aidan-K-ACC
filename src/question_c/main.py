#add import
import question_c

def question_c_menu():
    print("This program returns the sum of all even numbers\nthat fit within the parameter number.\nType 'EXIT' to quit.")
    runstate= "RUN"
    while runstate != "EXIT":
        num= input("Enter a number.\n")
        if num=="EXIT":
            runstate= "EXIT"
            print("Exiting...")
        else:
            print(question_c.get_sum_of_evens(int(num)))
        

question_c_menu()