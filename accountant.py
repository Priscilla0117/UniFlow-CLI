# store the files .txt to variables
Accountant_List = "Accountant_List.txt"
Student_Fees = "Student_Fees.txt"  # [0] for StudentID, [1] for StudentName, [2] for FeesCollected, [3] for TotatlFees
Fee_Receipts = "Fee_Receipts.txt"

# read each line of file
def read_file(filename):
    with open(filename, "r+") as file:
        return file.readlines()

def append_file(FileContentSt,filename):
    with open(filename,"a") as file:
        file.writelines(FileContentSt)

def write_file(FileContentSt,filename):
    with open(filename,"w") as file:
        file.writelines(FileContentSt)

def Record_Fees_Paid(filename):
    index = 0
    student_found = False
    FileContentSt = read_file(filename)
    StudentID = input("Please enter StudentID:")
    for lines in FileContentSt:
        line = lines.strip().split(",")
        if StudentID == line[0]:
            student_found = True
            paid_amount = float(input("Please enter amount paid:"))
            line[2] = float(line[2]) + paid_amount
            line[2] = str(line[2])
            FileContentSt.append(",".join(line)+"\n")
            del FileContentSt[index]
            fee_receipt = StudentID+","+str(paid_amount)+"\n"
            append_file(fee_receipt,Fee_Receipts)
            print("Successfully updated amount paid by student.")
            write_file(FileContentSt, filename)
            break
        index += 1
    if not student_found:
        print("Invalid ID entered. Please try again.")
        Record_Fees_Paid(filename)
    accountant_menu()

def View_Outstanding_Fees(filename):
    list_number = 1
    FileContentSt = read_file(filename)
    print("   StudentID      Name    Outstanding Fees")
    for lines in FileContentSt:
        line = lines.strip().split(",")
        if line[2] != line[3]:
            print(f"{list_number}. {line[0]}            {line[1]}    RM {float(line[3])-float(line[2])}")
        list_number += 1
    accountant_menu()

def Update_Payment_Records(filename):
    index = 0
    student_found = False
    FileContentSt = read_file(filename)
    StudentID = input("Please enter StudentID:")
    for lines in FileContentSt:
        line = lines.strip().split(",")
        if StudentID == line[0]:
            student_found = True
            updated_payment = float(input("Please enter new payment amount:"))
            line[3] = str(updated_payment)
            FileContentSt.append(",".join(line) + "\n")
            del FileContentSt[index]
            print("Successfully updated amount paid by student.")
            write_file(FileContentSt, filename)
            break
    if not student_found:
        print("Invalid Student ID entered. Please try again.")
        Update_Payment_Records(filename)
        index += 1
    accountant_menu()

def Issue_Fee_Receipts():
    FileContentSt = read_file(Fee_Receipts)
    StudentID = input("Please enter StudentID:")
    numbering = 1
    print(f"Receipts for StudentID {StudentID} are as follows:\n")
    print(f"No.   Fees Paid")
    for lines in FileContentSt:
        stuID ,fees_paid = lines.strip().split(",")
        if StudentID == stuID:
            print(f"{numbering}     {fees_paid}")
            numbering += 1
    accountant_menu()

def View_Financial_Summary(filename):
    FileContentSt = read_file(filename)
    student_found = False
    StudentID = input("Please enter StudentID:")
    for lines in FileContentSt:
        line = lines.strip().split(",")
        if StudentID == line[0]:
            student_found = True
            print("\n---   Student Summary   ---\n"
                  f"Student ID: {line[0]}\n"
                  f"Student Name: {line[1]}\n"
                  f"Total Fees: {float(line[3])}\n"
                  f"Fees Collected: {line[2]}\n"
                  f"Amount Payable: {float(line[3])-float(line[2])}\n")
            break
    if not student_found:
        print("Invalid Student ID entered! Please try again.")
        View_Financial_Summary(filename)
    accountant_menu()

def accountant_menu():
    print("----   Accountant Interface   ----\n\n"
          "1. Record Tuition Fees\n"
          "2. View Outstanding Fees\n"
          "3. Update Payment Records\n"
          "4. Issue Fee Receipt\n"
          "5. View Financial Summary\n"
          "6. Exit\n\n"
          "----   Accountant Interface   ----\n")
    option = input("Please enter the following option: (1-5)")

    if option == "1":
        Record_Fees_Paid(Student_Fees)
    elif option == "2":
        View_Outstanding_Fees(Student_Fees)
    elif option == "3":
        Update_Payment_Records(Student_Fees)
    elif option == "4":
        Issue_Fee_Receipts(Student_Fees)
    elif option == "5":
        View_Financial_Summary(Student_Fees)
    elif option == "6":
        import main_menu
        main_menu.main_menu()
    else:
        print("Invalid option entered! Please try again.")
        accountant_menu()
