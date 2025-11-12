module_file= "Available_Modules.txt"
enrollment_file= "Student_Modules.txt"
grade_file= "Student_Grade.txt"
attendance_file= "Student_Attendance.txt"
fees_file = "Student_Fees.txt"
#read file data
def read_file(file_name):
    with open(file_name,"r") as file:
        return file.readlines()

# write data to a file
def write_file(file_name,lines):
    with open(file_name,"w") as file:
        file.writelines(lines)

#append data to a file
def append_to_file(file_name,line):
    with open(file_name,"a") as file:
        file.writelines(line+"\n")

def confirmation(student_id):   # ask user whether to proceed with their current selection
    print("\n    Do you wish to proceed with this selection?\n"
          "                     1. Yes\n"
          "                     2. No\n")
    decision = input(">>>   ")
    if decision == "1":         # continue with the current selection
        return
    if decision == "2":         # return to menu
        student_menu(student_id)

# 1. View Available Modules
def view_available_modules():
    available_modules = read_file(module_file)
    print("-------------------------------------------------------------"
          "\n{:<12} {:<40} {:>6}".format("Module ID", "Module Name", "Credit" + "\n"
            "-------------------------------------------------------------"))
    for modules in available_modules:
        mID, mName, mProg = modules.strip().split(",")
        print("{:<12} {:<40} {:>6}".format(mID, mName, mProg))
    print("\n-------------------------------------------------------------\n")

# 2. Enrol in module
def enrol_in_module(student_id):
    index = 0
    student_file_content = read_file(enrollment_file)
    module_id = input("Please enter module ID:")
    for lines in student_file_content:
        line = lines.strip().split(",")
        if student_id  == line[0]:
            if module_id in line[2:]:
                print(f"Error! The course with course ID {module_id} is already registered. Please try again.")
            if module_id not in line[2:]:
                del student_file_content[index]
                student_file_content.append(",".join(line)+f",{module_id}\n")
                print(f"You are now registered under the course with course ID {module_id}.")
                write_file(enrollment_file,student_file_content)
                break
        index += 1

# 3. View Grades
def view_grades(student_id):
    grades = read_file(grade_file)
    print("\nYour Grades:")
    found = False
    for grade in grades:
        stored_id,student_name,module,mark= grade.strip().split(",")
        if stored_id == student_id:
            print(f"{module} : {mark}")
            found=True
    if not found:
        print("Your ID's grades were not found.")

# 4. Access Attendance Record
def access_attendance_record(student_id):
    attendance=read_file(attendance_file)
    print("\nAttendance Record:\n")
    found=False
    print("{:<12} {:<10} {:<40} {:<12}".format("Date", "Time", "Module", "Attendance"))
    for record in attendance:
        stored_id,module,attendance,date,time =record.strip().split(",")
        if student_id == stored_id:
            print("{:<12} {:<10} {:<40} {:<12}".format(date,time,module,attendance))
            found=True
    if not found:
        print("Your ID's attendance record was not found.")

# 5. Unenroll from Module
def unenroll_from_module(student_id):
    index = 0
    module_code = input("Enter your module code to unenroll:").strip()
    student_file_content = read_file(enrollment_file)
    for lines in student_file_content:
        line = lines.strip().split(",")
        if student_id == line[0]:
            if module_code in line[2:]:
                line.remove(module_code)
                del student_file_content[index]
                print("You have successfully unenrolled from this module.")
                student_file_content.append(",".join(line) + "\n")
                write_file(enrollment_file, student_file_content)
                break
            else:
                print("You are not enrolled in this module.")
            index += 1

def view_outstanding_fees(entered_id):
    FileContentSt = read_file(fees_file)
    student_found = False
    for lines in FileContentSt:
        student_id,student_name,fees_paid,total_fees = lines.strip().split(",")
        if entered_id == student_id:
            student_found = True
            print("\n---   Student Summary   ---\n"
                  f"Student ID: {student_id}\n"
                  f"Student Name: {student_name}\n"
                  f"Total Fees: {float(total_fees)}\n"
                  f"Fees Collected: {fees_paid}\n"
                  f"Amount Payable: {float(total_fees) - float(fees_paid)}\n")
            break
    if not student_found:
        print("Your fees record could not be found. Please contact university accountant for more details.")

    # Main menu
def student_menu(student_id):
    while True:
        print("")
        print("1. View Available Modules\n"
              "2. Enroll in Module\n"
              "3. View Grades\n"
              "4. Access Attendance Record\n"
              "5. Unenroll from Module\n"
              "6. View Outstanding Fees\n"
              "7. Exit")
        option = input("Enter your choice:")
        if option == '1':
            confirmation(student_id)
            view_available_modules()
        elif option == '2':
            confirmation(student_id)
            enrol_in_module(student_id)
        elif option == '3':
            confirmation(student_id)
            view_grades(student_id)
        elif option == '4':
            confirmation(student_id)
            access_attendance_record(student_id)
        elif option == '5':
            confirmation(student_id)
            unenroll_from_module(student_id)
        elif option == '6':
            confirmation(student_id)
            view_outstanding_fees(student_id)
        elif option == '7':
            confirmation(student_id)
            import main_menu
            main_menu.main_menu()
        else:
            print("Invalid choice, please try again.")
