import question_a

def question_a_menu():
    print("This program determines a person's title based on age.\nType 'EXIT' to quit.")
    runstate= "RUN"
    while runstate != "EXIT":
        age= input("Enter an age.\n")
        if age=="EXIT":
            runstate= "EXIT"
            print("Exiting...")
        else:
            print(question_a.get_person_category(float(age)))
        

question_a_menu()