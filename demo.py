def main():
    student = get_student()
    print(f"{student['First Name']} {student['Last Name']}")

def get_student():
    student = {"First Name": None, "Last Name": None}
    student["First Name"] = input("Enter your first name: ")
    student["Last Name"] = input("Enter your last name: ")
    return student

if __name__ == "__main__":
    main()