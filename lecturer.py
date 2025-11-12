Lecturer_Details = "Lecturer_Details.txt"
Student_Details = "Student_Details.txt"
Student_List = "Student_Modules.txt"
Student_Attendance = "Student_Attendance.txt"
Student_Grade = "Student_Grade.txt"
Available_Modules = "Available_Modules.txt"

import time                                                         # time and seconds function
import datetime                                                    # track date and time for attendance
current_date = datetime.datetime.now().date()                       # assign the current date to a variable
current_time = datetime.datetime.now().strftime("%H:%M")                # assign the current time to a variable
lecturerline = "-------------- Lecturer's Interface --------------"

def append_file(filename,new_content):
    with open(filename,"a") as file:    # opens filename passed in the argument in append mode
        file.write(new_content)         # write content passed in the argument into the file

def read_file(filename):
    with open(filename,"r") as file:    # opens filename passed in argument in read mode
        return file.readlines()         # read each line in the file return the content read

def invalid_answer():                                   # call function when an invalid input is entered.
    print(">>>   Invalid input. Please try again.")
    time.sleep(0.6)

def rerun(entered_id):                                                              # ask user whether to continue using the same functionality or return to menu
    while True:
        print("\n             Would you like to continue?\n"
              "                          1. Yes\n"
              "                          2. No\n"
              f"\n{lecturerline}")
        decision = input(">>>   ")
        if decision == "1":
            return                                                                              # return to the previous function and repeat by iterating the while True loop
        elif decision == "2":
            print(">>>   Exiting...")
            time.sleep(0.4)
            lecturer_menu(entered_id)                                   # return to menu
        else:
            invalid_answer()

def confirmation(entered_id):                                               # ask user whether to proceed with their current selection
    while True:
        print("\n    Do you wish to proceed with this selection?\n"
              "                     1. Yes\n"
              "                     2. No\n")
        decision = input(">>>   ")
        if decision == "1":                                                 # continue with the current selection
            return
        elif decision == "2":                                               # return to menu
            lecturer_menu(entered_id)
        else:
            invalid_answer()

def validate_student_modules(input_studentID,selected_module_id):
    enrolled_modules = read_file(Student_List)
    found = False
    for lines in enrolled_modules:
        line = lines.strip().split(",")
        student_id, student_name, student_modules = line[0], line[1], line[2:]
        if input_studentID == student_id:
            if selected_module_id in student_modules:
                found = True
                return found, student_name, None
            else:
                message = f">>>   The student is not enrolled in the module selected."
                return found, student_name, message
    if not found:
        message = f">>>   The student's enrolled modules data does not exist."
        return found, None, message

def assigned_modules_identifier(entered_id,lecturer_file,modules_file):
    identified_courses = []
    lecturer_details = read_file(lecturer_file)                                                             # parse file content of "Lecturer_Details.txt"
    available_modules = read_file(modules_file)                                                                 # parse file content of "Available_Modules.txt"
    for lines in lecturer_details:
        lectline = lines.strip().split(",")
        lecturer_id = lectline[0]
        assigned_modules_id = lectline[2:]
        if entered_id == lecturer_id:                                                                       # if entered_id tally with details in "Lecturer_Details.txt"
            for assigned_module_id in assigned_modules_id:                                                          # for each of the lecturer's assigned modules
                for entries in available_modules:                                                                   # for each line of module details in "Available Modules"
                    entry = entries.strip().split(",")
                    module_id, module_name = entry[0], entry[1]
                    if assigned_module_id == module_id:
                        identified_courses.append(module_id+","+module_name+"\n")
    return identified_courses

def lecturer_view_modules(entered_id,lecturer_file,modules_file):                                       # view modules currently assigned to lecturer
    lecturer_assigned_modules = assigned_modules_identifier(entered_id,lecturer_file,modules_file)                                                                                           # empty list to insert currently assigned modules
    print(">>>   Viewing assigned modules...\n")
    time.sleep(0.5)
    print(f"{lecturerline}\n"
              "Your assigned modules:\n")
    numbering = 1
    for modules in lecturer_assigned_modules:
        module_id, module_name = modules.strip().split(",")
        print(f"{numbering}. {module_name}")
        numbering += 1
    return
    
def module_selector(entered_id,lecturer_file,modules_file):     #
    while True:
        try:
            lecturer_view_modules(entered_id, lecturer_file, modules_file)
            assigned_modules = assigned_modules_identifier(entered_id, lecturer_file, modules_file)
            module_choice = int(input("\n>>>   Please select module: ")) - 1
            print(f"\n{lecturerline}")
            selected_module = assigned_modules[module_choice].strip().split(",")
            return selected_module
        except ValueError:
            print(">>>   Invalid input entered! Please try again!\n\n")
        except IndexError:
            print(">>>   Invalid option entered. Please try again!")

def lecturer_record_grades(entered_id,lecturer_file,modules_file,grades_file):
    while True:
        selected_module_id, selected_module_name = module_selector(entered_id,lecturer_file,modules_file)
        print(f"Module Selected - {selected_module_name}\n")
        input_studentID = input(">>>   Please enter student ID: ")
        student_found, student_name, message = validate_student_modules(input_studentID,selected_module_id)
        if student_found is True:
            while True:
                grade = input(">>>   Please choose student grade from A/B/C/D/E/F: ")
                if grade.upper() in ('A','B','C','D','E','F'):
                    new_entry = f"\n{input_studentID},{student_name},{selected_module_name},{grade}"
                    append_file(grades_file,new_entry)
                    print("\n>>>   Student's grades successfully recorded.")
                    break
                else:
                    print("")
                    invalid_answer()
        else:
            print(message)
        rerun(entered_id)

# LECTURER'S VIEW STUDENT GRADE FUNCTION
def lecturer_view_student_grades(entered_id,lecturer_file,modules_file,grades_file):
        while True:
            selected_module_id, selected_module_name = module_selector(entered_id,lecturer_file,modules_file)
            print(f"Module Selected - {selected_module_name}\n")
            grades_file_content = read_file(grades_file)
            x=1
            print(f"{'Student ID':<15} {"Student Name":<25} {'Grade':<5}")
            for lines in grades_file_content:
                student_id,student_name,module_name,grade = lines.strip().split(",")
                if module_name == selected_module_name:
                    print(f"{student_id:<15} {student_name:<25} {grade:<5}")
                    x=x+1
            rerun(entered_id)

# LECTURER'S TRACK ATTENDANCE FUNCTION
def lecturer_track_attendance(entered_id,lecturer_file,modules_file,student_attendance_file):
    while True:
        try:
            selected_module_id, selected_module_name = module_selector(entered_id,lecturer_file,modules_file)
            print(f"Module Selected - {selected_module_name}\n")
            input_studentID = input(">>>   Please enter student ID: ")  # lecturer input
            student_found, student_name, message = validate_student_modules(input_studentID,selected_module_id)
            if student_found is True:
                while True:
                    attendance_types = ('Present','Late','Absent')
                    print(">>>   Please mark student attendance:\n\n"
                          "1. Present\n"
                          "2. Late\n"
                          "3. Absent\n")
                    attendance = int(input(">>>   ")) - 1
                    if attendance < len(attendance_types):
                        new_attendance_entry = f"\n{input_studentID},{selected_module_name},{attendance_types[attendance]},{current_date},{current_time}"
                        append_file(student_attendance_file,new_attendance_entry)
                        print("\n>>>   Student's attendance successfully recorded.")
                        break
                    else:
                        print("")
                        invalid_answer()
            else:
                print(message)
            time.sleep(0.4)
            rerun(entered_id)
        except ValueError:
            invalid_answer()

# LECTURER'S VIEW STUDENT LIST FUNCTION
def lecturer_view_student_list(entered_id,lecturer_file,modules_file,student_list_file):
    while True:
        numbered_list = 1
        selected_module_id, selected_module_name = module_selector(entered_id,lecturer_file,modules_file)
        print(f"Module Selected - {selected_module_name}\n")
        student_list = read_file(student_list_file)
        for student_lines in student_list:
            student_line = student_lines.strip().split(",")
            input_studentID, student_name, enrolled_modules = student_line[0], student_line[1], student_line[2:]
            student_found, _, message = validate_student_modules(input_studentID,selected_module_id)
            if student_found is True:
                print(f"{numbered_list}. {student_name}")
                numbered_list += 1
        rerun(entered_id)

def lecturer_menu(entered_id):
    while True:
        print(f"\n{lecturerline}\n" 
              "\nSelect your actions:\n"
              "\n1. View Assigned Modules\n"
              "2. Record Grades\n"
              "3. View Student List\n"
              "4. Track Attendance\n"
              "5. View Student Grades\n"
              f"6. Exit\n\n{lecturerline}")
        lecture_selection = input(">>>   ")
        if lecture_selection == "1":
            lecturer_view_modules(entered_id,Lecturer_Details,Available_Modules)
            time.sleep(3)
            lecturer_menu(entered_id)
        elif lecture_selection == "2":
            confirmation(entered_id)
            lecturer_record_grades(entered_id,Lecturer_Details,Available_Modules,Student_Grade)
        elif lecture_selection == "3":
            confirmation(entered_id)
            lecturer_view_student_list(entered_id,Lecturer_Details,Available_Modules,Student_List)
        elif lecture_selection == "4":
            confirmation(entered_id)
            lecturer_track_attendance(entered_id,Lecturer_Details,Available_Modules,Student_Attendance)
        elif lecture_selection == "5":
            confirmation(entered_id)
            lecturer_view_student_grades(entered_id,Lecturer_Details,Available_Modules,Student_Grade)
        elif lecture_selection == "6":
            print(">>>   Logging out...")
            time.sleep(0.5)
            print(">>>   Successfully logged out.")
            time.sleep(0.5)
            import main_menu
            main_menu.main_menu()
        else:
            print(">>>   Invalid option entered. Please try again.")
            time.sleep(0.5)
