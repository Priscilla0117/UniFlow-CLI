# Registrar
# • Register New Students: Record new student details (name, student ID, program).
# • Update Student Records: Edit details of students, such as program or contact information.
# • Manage Enrolments: Update module enrolments for students.
# • Issue Transcripts: Summarize and generate a transcript for specific students.
# • View Student Information: Access detailed student records for verification or updates.

# Registrar Menu


# File Name
registrar_list = "list.txt"
student_record = "Student_Details.txt"
module = "Available_Courses.txt"
student_grade = "Student_Grade.txt"


def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines() #Return read files from text file
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None


def write_file(filename, content_list):
    with open(filename, 'w') as file:
        for entry in content_list:
            if isinstance(entry, list):  # Handle nested lists if needed
                file.write(','.join(entry) + '\n')
            else:
                file.write(entry + '\n')


# TODO:
def append_file(filename, content):
    with open(filename, "a") as file:
        # Handle if content is a string
        if isinstance(content, str):
            file.write(content + "\n")
        # Handle if content is a list
        elif isinstance(content, list):
            file.write(",".join(map(str, content)) + "\n")
        else:
            raise ValueError("Unsupported content type for writing to file.")


def validate_input(prompt):
    while True:
        if prompt:
            if isinstance(prompt, str):
                value = prompt.strip()
            else:
                value = prompt

            return value

        else:
            print("Input is required")
            return

def registrar_menu():
    while True:
        try:
            opt_number_registrar = int(input("""
Registrar Interface
1. Register New Students
2. Update Student Records
3. Manage Enrolments
4. Issue Transcripts
5. View Student Information
6. Exit
Enter the option number: """))

            match opt_number_registrar:
                case 1:
                    register_new_student(student_record)
                case 2:
                    update_student_records(student_record)
                case 3:
                    manage_enrolments(module)
                case 4:
                    generate_transcript(student_grade)
                case 5:
                    view_student_information(student_record)
                case 6:
                    print("Exiting the Registrar Menu...")
                    import main_menu
                    main_menu.main_menu()
                case _:
                    print("Invalid option number")
        except ValueError:
            print("Invalid option number")
            # Ask if the user wants to continue after each operation

def register_new_student(filename):
    try:
        file_content = read_file(filename)
        student_id = input("Enter student ID: ")
        for line in file_content:
            student_id_line = line.strip().split(', ')
            if student_id == student_id_line[0]:
                print("Student ID already exists. Please try again.")
                return

        name = input("Enter student name: ")
        program = input("Enter program: ")
        course = input("Enter course: ")
        contact_info = input("Enter email address: ")

        validate_input(student_id)
        validate_input(name)
        validate_input(program)
        validate_input(course)
        validate_input(contact_info)

        data = [student_id, name, program, course, contact_info]
        data = ",".join(data)

        append_file(filename, data)

        print("New student registered successfully")

    except ValueError:
        print("Invalid input. Please try again.")

# TODO: Add exception when blank input is added for registration


def update_student_records(filename):
    file_content = read_file(filename)
    student_id_input = input("Enter Student ID: ").strip()
    validate_input(student_id_input)

    data_list = []
    student_found = False

    for line in file_content:
        student_id, name, program, course, contact_info = line.strip().split(', ')

        if student_id == student_id_input:
            student_found = True
            print(f"Updating details for student with ID: {student_id}")
            update_menu = """
    1. Name
    2. Program
    3. Course
    4. Email
    5. Exit
                """
            option = input(f"Choose field to update: \n {update_menu} \n Option number: ").strip()
            validate_input(option)

            if option == "1":
                name = input("Enter new name: ").strip()
            elif option == "2":
                program = input("Enter new program: ").strip()
            elif option == "3":
                course = input("Enter new course: ").strip()
            elif option == "4":
                contact_info = input("Enter new email: ").strip()
            elif option == "5":
                print("Exiting Update Student Records...")
                return
            else:
                print("Invalid option.")
                continue

            print("Record updated successfully. \n")
        data_list.append(f"{student_id}, {name}, {program}, {course}, {contact_info}")

    if not student_found:
        print(f"No student found with ID: {student_id_input}")

    write_file(filename, data_list)




#TODO: Update
def manage_enrolments(filename):
    # Helper functions
    def read_modules_from_file():
        """Read file content and return a dictionary of courses with modules."""
        content = read_file(filename)
        courses = {}
        for line in content:
            parts = line.strip().split(",")
            courses[parts[0]] = parts[1:]  # Course code is the key, modules are the values
        return courses

    def write_modules_to_file(courses):
        """Write the courses dictionary back to the file."""
        content_list = [f"{course},{','.join(modules)}" for course, modules in courses.items()]
        write_file(filename, content_list)

    def add_module():
        counter = 0
        courses = read_modules_from_file()
        course_code = input("Enter the course code: ").upper()
        validate_input(course_code)

        if course_code not in courses:
            print("Course not found.")
            return

        number_of_modules = int(input("How many modules to add? "))
        for _ in range(number_of_modules):
            counter += 1
            module_name = input(f"Enter module name {counter}: ").strip()
            validate_input(module_name)
            if module_name in courses[course_code]:
                print(f"Module '{module_name}' already exists.")
            else:
                courses[course_code].append(module_name)
                print(f"Module '{module_name}' added.")

        write_modules_to_file(courses)
        print("Modules updated successfully.")

    def remove_module():
        courses = read_modules_from_file()
        course_code = input("Enter the course code: ").upper()
        validate_input(course_code)

        if course_code not in courses:
            print("Course not found.")
            return

        module_name = input("Enter the module name to remove: ").strip()
        validate_input(module_name)

        if module_name in courses[course_code]:
            courses[course_code].remove(module_name)
            print(f"Module '{module_name}' removed.")
        else:
            print("Module not found.")

        write_modules_to_file(courses)

    def add_course():
        counter = 0
        courses = read_modules_from_file()
        course_code = input("Enter the course code: ").upper()
        validate_input(course_code)

        if course_code in courses:
            print("Course already exists.")
            return

        number_of_modules = int(input("How many modules to add? "))
        modules = []
        #
        for _ in range(number_of_modules):
            counter += 1
            module_name = input(f"Enter module name {counter}: ").strip()
            validate_input(module_name)
            modules.append(module_name)

        courses[course_code] = modules
        write_modules_to_file(courses)
        print(f"Course '{course_code}' added successfully.")

    def remove_course():
        courses = read_modules_from_file()
        course_code = input("Enter the course code: ").upper()
        validate_input(course_code)

        if course_code in courses:
            del courses[course_code]
            print(f"Course '{course_code}' removed successfully.")
        else:
            print("Course not found.")

        write_modules_to_file(courses)

    # Main menu for managing enrollments
    while True:
        try:
            option = int(input("""
    Manage Enrollments Menu:
    1. Add Module
    2. Remove Module
    3. Add Course
    4. Remove Course
    5. Exit
    Enter option number: """))

            match option:
                case 1:
                    add_module()
                case 2:
                    remove_module()
                case 3:
                    add_course()
                case 4:
                    remove_course()
                case 5:
                    print("Exiting Manage Enrollments Menu...")
                    break
                case _:
                    print("Invalid option.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")





def generate_transcript(file_path):
    transcript = []

    student_id = input("Enter the student ID: ")

    # Step 1: Read the file and filter records for the specific student
    lines = read_file(file_path)

    for line in lines:
        parts = line.strip().split(',')
        current_id, name, subject, grade = parts
        if current_id == student_id:
            student_name = name
            transcript.append((subject, grade))

    # Step 2: Check if the student was found
    if not transcript:
        print(f"No records found for student ID: {student_id}")
        return

    # Step 3: Generate and print the transcript
    print(f"Transcript for {student_name} (ID: {student_id})")
    print("=" * 50)
    print(f"{'Subject':<40} {'Grade':<40}")
    print("-" * 50)
    for subject, grade in transcript:
        print(f"{subject:<40} {grade:<40}")
    print("=" * 50)


# TODO:
# View Student Information
def view_student_information(filename):
    student_id = input("Enter student ID: ")

    # Read the file and filter records for the specific student
    lines = read_file(filename)
    for line in lines:
        parts = line.strip().split(',')
        current_id, name, program, course, contact_info = parts

        if current_id == student_id:
            print(f"Student ID: {current_id}")
            print(f"Name: {name}")
            print(f"Program: {program}")
            print(f"Course: {course}")
            print(f"Contact Information: {contact_info}")
            return

    print(f"No records found for student ID: {student_id}")


registrar_menu()
