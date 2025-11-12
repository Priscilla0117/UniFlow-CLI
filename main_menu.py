import time
Login_Details = "Login_Details.txt"

def read_file(filename):
    with open(filename,"r") as file:
        return file.readlines()

def login(login_details_file):
    while True:
        wrong_counter = 0
        while wrong_counter < 3:
            entered_id = input("Please enter your ID: ")
            entered_password = input("Please enter your password: ")
            print("\n>>>   Logging in...")
            time.sleep(0.2)
            file_content = read_file(login_details_file)
            for line in file_content:
                stored_id, stored_password = line.strip("\n").split(",")
                if entered_id == stored_id and entered_password == stored_password:
                    print(">>>   Logged in successfully.\n")
                    time.sleep(0.5)
                    if entered_id[0] == "0":
                        import lecturer
                        lecturer.lecturer_menu(entered_id)
                    elif entered_id[0] == "1":
                        import student
                        student.student_menu(entered_id)
                    elif entered_id[0] == "2":
                        import administrator
                        administrator.administrator_menu()
                    elif entered_id[0] == "3":
                        import registrar
                        registrar.registrar_menu()
                    elif entered_id[0] == "4":
                        import accountant
                        accountant.accountant_menu()
                    return entered_id
            else:
                print(
                    f">>>   Invalid password or ID. Please try again.\n")
                time.sleep(0.5)
                wrong_counter += 1
        print(">>>   Too many attempts. The program has been locked for 30 seconds.")
        time.sleep(30)
        main_menu()

def main_menu():
    while True:
        print("\n------ Welcome to Asia Pacific University Management System (UMS) ------\n"
              "\n                        User Login Interface\n"
              "\n1. Login\n"
              "2. Exit\n"
              "\n------ Welcome to Asia Pacific University Management System (UMS) ------")
        selection = input(">>>    ")
        if selection == "1":
            login(Login_Details)
        elif selection == "2":
            print("\n                         Program Terminated."
                  "\n   Thank you for using Asia Pacific University Management System (UMS). ")
        else:
            print(">>>   Invalid input entered. Please try again.")
            time.sleep(0.5)
            break
        break
main_menu()