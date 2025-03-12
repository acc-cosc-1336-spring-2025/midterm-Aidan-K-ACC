#add import
import question_d

def question_d_menu():
    print("This program reverses text and returns it.\nType 'EXIT' to quit.")
    runstate= "RUN"
    while runstate != "EXIT":
        string= input("Enter some text.\n")
        if string=="EXIT":
            runstate= "EXIT"
            print("Exiting...")
        else:
            print(question_d.reverse_string(string))
        

question_d_menu()