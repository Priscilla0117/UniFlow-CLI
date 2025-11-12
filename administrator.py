##Administrator
##• Add New Module: Add module details (Module code, name, credits)
##• Add/Remove Students: Add new student details (ID, name, course programme) or remove
# them.
# • Manage Lecturers: Add or remove lecturers and update their information.
# • Generate Reports: Generate reports on total students, active courses, and faculty.
# • View All Data: Display all data across students, courses, and lecturers for administrative
# review.

Available_Courses = "Available_Modules.txt"
Lecturer_Details = "Lecturer_Details.txt"
Login_Details = "Login_Details.txt"
Student_Details = "Student_Modules.txt"

import time

breakcheck = False


def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def append_file(filename, content):
    with open(filename, 'a') as file:
        file.writelines(content)


def administrator_menu():
    while True:
        print("1. Add course", "\n2. View Course", "\n3. Add students",
              "\n4. Remove students", "\n5. Add lecturer", "\n6. Remove lecturer",
              "\n7. Update lecturer information", "\n8. Report", "\n9. View",
              "\n10. Exit")
        choice = input("Input your choice here: ")
        if choice == '1':
            add_module(Available_Courses)
        elif choice == '2':
            view_course(Available_Courses)
        elif choice == '3':
            add_student()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            add_lecturer(Lecturer_Details)
        elif choice == '6':
            remove_lecturer(Lecturer_Details)
        elif choice == '7':
            update_lecturer_records('Lecturer_Details.txt')
        elif choice == '8':
            report()
        elif choice == '9':
            view()
        elif choice == '10':
            import main_menu
            main_menu.main_menu()
        else:
            print("Invalid choice. Please try again.")


def validateDuplicateID(instanceFile, IDentered):
    instanceFile = instanceFile.readlines()
    for line in instanceFile:
        arraySplit = line.split(",")
        if len(arraySplit) > 0:
            foundID = arraySplit[0]
            if str.lower(str(foundID)) == str.lower(str(IDentered)):
                return True
    return False


def add_module(available_module):
    mID = input("Please enter new module ID:").strip()
    mName = input("Please enter new module name:")
    mCred = input("Please enter new module credit:").strip()
    with open(available_module, "r") as validationFile:
        if not validateDuplicateID(validationFile, mID):
            append_file(available_module, f"{mID},{mName},{mCred}" + "\n")
            print(f"Module with ID {mID} has been created!")
        else:
            print(f"Module with ID {mID} already exist!")


def view_course(available_courses):
    file_content = read_file(available_courses)
    print("\n{:<12} {:<40} {:>6}".format("Module ID", "Module Name", "Credit"))
    for lines in file_content:
        mID, mName, mProg = lines.strip().split(",")
        print("{:<12} {:<40} {:>6}".format(mID, mName, mProg))
    print("")


def add_student():
    with open("Student_Modules.txt", "a") as Stu:
        with open("Student_Modules.txt", "r") as txtFile:
            newStuID = input("Please enter new student ID: ")
            newStuName = input("Please enter new student name: ")
            newStuCourse = input("Please enter new student's course programme:")

            def getValidModules(moduleName):
                with open('Available_Modules.txt', 'r') as courseFile:
                    valid_modules = []
                    courses = courseFile.readlines()
                    for course in courses:
                        course_data = course.strip().split(",")
                        if course_data[0] == moduleName:
                            valid_modules.append(moduleName)
                            break

                    if not validateDuplicateID(txtFile, newStuID):
                        if valid_modules:
                            Stu.write(newStuID + "," + newStuName+"\n")
                            append_file(Login_Details, f"{newStuID},abc")
                            print(f"Student with ID {newStuID} added successfully.")
                        else:
                            print(
                                f"Student with ID {newStuID} failed to be added as course programme entered doesn't exist.")
                    else:
                        print(f"Student with ID {newStuID} already exists!")
                    return

            getValidModules(newStuCourse)


def remove_student():
    def remove_line(file_path, target_line_content):
        updated_lines = []

        # Read all lines from the file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Filter out the line containing the target content
        isDeleted = False
        for line in lines:
            stuline = line.split(",")
            if stuline[0] != target_line_content:  # Keep lines that don't match
                updated_lines.append(line)
            else:
                isDeleted = True
        # Write the updated lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        if isDeleted:
            print(f"Student with the ID '{target_line_content}' has been removed.")
        else:
            print(f"Student with the ID '{target_line_content}' does not exist!")

    target_line_content = input("ID to remove : ")
    remove_line('Student_Modules.txt', target_line_content)


def add_lecturer(lecturer_details):
    lectID = input("Please enter new lecturer ID:").strip()
    lectName = input("Please enter new lecturer name:").strip()
    with open(lecturer_details, "r") as validationFile:
        if not validateDuplicateID(validationFile, lectID):
            append_file(lecturer_details, f"{lectID},{lectName}" + "\n")
            append_file(Login_Details, f"{lectID},abc" + "\n")
            print(f"Lecturer with ID {lectID} added successfully.")
        else:
            print(f"Lecturer with ID {lectID} already exists!")


def update_lecturer_records(filename):
    data_list = []

    # Prompt for Lecturer ID
    lecturer_id = input("Enter Lecturer ID: ")

    # Read the content of lecturer.txt file and add them to list
    file_content = read_file(filename)
    for line in file_content:
        parts = line.strip().split(",")
        data_list.append(parts)

    # Update Lecturer Data Menu
    update_lecturer_record_menu = input(
        """Change Option:
        1. Name
        2. Modules
        3. Exit
        Input Option Number: """)

    # Scan for target Lecturer ID and modify/verify
    lecturer_found = False
    for data in data_list:
        if data[0] == lecturer_id:
            lecturer_found = True
            print(f"Updating details for lecturer with ID: {lecturer_id}")
            break

    if not lecturer_found:
        print("Lecturer not found.")
        return

    # Update based on menu selection
    match update_lecturer_record_menu:
        case '1':
            splittedStr = []
            for key in data:
                splittedStr.append(key)
            if len(",".join(splittedStr).split(",")) >= 1:
                new_name = input("Enter new lecturer name: ").capitalize()
                data[1] = new_name
                print("Lecturer's name updated successfully.")
            else:
                print("Lecturer does not exist !")
                return
        case '2':
            # Step 2: Get a list of module codes to assign
            modules = input("Enter the module codes to assign (separate by commas): ").split(",")
            modules = [module.strip() for module in modules]  # Clean any extra spaces
            # Step 3: Read the lecturer file to get current lecturer details
            with open('Lecturer_Details.txt', 'r') as lec_file:
                lecturers = lec_file.readlines()
            # Check if the lecturer exists
            lecturer_found = False
            for i in range(len(lecturers)):
                lecturer_data = lecturers[i].strip().split(",")
                if lecturer_data[0] == lecturer_id:
                    lecturer_found = True
                    break
            if not lecturer_found:
                print(f"Lecturer with ID {lecturer_id} not found.")
                return
            # Step 4: Read the courses and check if they exist
            with open('Available_Modules.txt', 'r') as course_file:
                courses = course_file.readlines()
            valid_modules = []
            for module in modules:
                module_found = False
                for course in courses:
                    course_data = course.strip().split(",")
                    if course_data[0] == module:
                        module_found = True
                        valid_modules.append(module)
                        break
                if not module_found:
                    print(f"Module with code {module} not found.")
            # Step 5: If there are valid modules, assign them to the lecturer
            if valid_modules:
                updated_line = f"{lecturer_data[0]},{lecturer_data[1]},{','.join(valid_modules)}\n"
                lecturers[i] = updated_line  # Update the lecturer's entry with the assigned modules

                # Write the updated data back to the file
                with open('Lecturer_Details.txt', 'w') as lec_file:
                    lec_file.writelines(lecturers)
                print(f"Modules {', '.join(valid_modules)} have been updated to lecturer {lecturer_data[0]}.")
            return
        case '3':
            print("Exiting Update Lecturer Records...")
            return
        case _:
            print("Invalid option, please try again.")
            return

    # Write the updated data back into the file
    with open('Available_Modules.txt', 'r') as course_file:
        courses = course_file.readlines()

    with open(filename, 'w') as file:
        for line in data_list:
            file.writelines(",".join(line) + "\n")

    print("Lecturer information updated successfully.")


def remove_lecturer(lecturer_details):
    def remove_line(file_path, target_line_content):
        updated_lines = []

        # Read all lines from the file
        lines = read_file(file_path)
        # Filter out the line containing the target content
        isDeleted = False
        for line in lines:
            arraySplit = line.split(",")
            if len(arraySplit) > 0:
                idFound = arraySplit[0]
                if idFound != target_line_content:  # Keep lines that don't match
                    updated_lines.append(line)
                else:
                    isDeleted = True
            else:
                print(f"Lecturer does not exist!")
        # Write the updated lines back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        if file_path == Lecturer_Details:
            if isDeleted:
                print(f"Lecturer with the ID '{target_line_content}' has been removed.")
            else:
                print(f"Lecturer with the ID '{target_line_content}' does not exist!")
        else:
            pass

    target_line_content = input("Please enter lecturer ID to remove:")
    remove_line(lecturer_details, target_line_content)
    remove_line(Login_Details, target_line_content)


def report():
    with open('Student_Modules.txt', 'r'):
        print(f"Current active students:    {len(read_file('Student_Modules.txt'))} students.")
    with open('Lecturer_Details.txt', 'r'):
        print(f"Current active lecturers:   {len(read_file('Lecturer_Details.txt'))} lecturers.")
    with open('Available_Modules.txt', 'r'):
        print(f"Current active courses:    {len(read_file('Available_Modules.txt'))} active courses.")
        time.sleep(3)


def view():
    student_file_content = read_file(Student_Details)
    courses_file_content = read_file(Available_Courses)
    lecturer_file_content = read_file(Lecturer_Details)

    def all_student_info():
        print("\n-------------------------------------------------------------"
              "\n{:<12} {:<40}".format("Student ID", "Student Name","\n"
                                                                                      "-------------------------------------------------------------"))
        for student_entries in student_file_content:  # displaying student details
            student = student_entries.strip().split(",")
            stuID, stuName = student[0], student[1]
            print("{:<12} {:<40} ".format(stuID, stuName))
        print("\n-------------------------------------------------------------\n")

    def all_courses_info():
        print("-------------------------------------------------------------"
              "\n{:<12} {:<40} {:>6}".format("Course ID", "Course Name", "Credit" + "\n"
                                                            "-------------------------------------------------------------"))
        for courses_entries in courses_file_content:
            mID, mName, mProg = courses_entries.strip().split(",")
            print("{:<12} {:<40} {:>6}".format(mID, mName, mProg))
        print("\n-------------------------------------------------------------\n")

    def all_lecturer_info():
        for lecturer_entries in lecturer_file_content:
            lecturer_entry = lecturer_entries.strip().split(",")
            print("-------------------------------------------------------------"
                "\n{:<12} {:<40}".format("Lecturer ID", "Lecturer Name")+"\n"
                "-------------------------------------------------------------\n"
                "{:<12} {:<40}".format(lecturer_entry[0], lecturer_entry[1])+"\n\n"
                   "Assigned Modules:\n")
            given_courses = lecturer_entry[2:]
            for course in given_courses:
                for courses_entries in courses_file_content:
                    course_entry = courses_entries.strip().split(",")
                    if course_entry[0] == course:
                        print(course_entry[1])
        print("-------------------------------------------------------------\n")

    print("\nPlease select section to view:\n"
          "1. Students\n"
          "2. Courses\n"
          "3. Lecturers\n"
          "4. Exit")
    user_selection = input(">>>   ")

    if user_selection == "1":  # display all student information
        all_student_info()
    elif user_selection == "2":  # display all courses information
        all_courses_info()
    elif user_selection == "3":  # display all lecturer information
        all_lecturer_info()
    elif user_selection == "4":  # exit to admin menu
        administrator_menu()
    else:
        print("Invalid option entered. Please try again")
        time.sleep(0.4)
        view()


administrator_menu()

