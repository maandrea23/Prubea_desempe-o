from validations import inputValidator, add_student,show_student, search_student, update_student, delete_student,status
from persistencia import save_csv, load_csv

def choose(option, student_list):
    # Processes menu option with validations
    match option:
        case 1:
            Id = inputValidator (int,"ID: ", "must be a number, not letter")
            name = inputValidator(str, "Student name: ", "cannot be empty.")
            age = inputValidator(int, "Age: ", "must be >0.")
            course = inputValidator(str, "Course or program: ", "cannot be empty.")
            statu = status()
            add_student(student_list,Id,name,age,course,statu)
        case 2:
            show_student(student_list)
        case 3:
            Id = int(input("ID to search: "))
            search_student(student_list, Id)
        case 4:
            Id = int(input("Id to update: "))
            name_n = input("New name: ").strip()
            age_n = input("New age: ")
            course_n = input ("New course: ").strip()
            status_n = int(input ("New status, 1. Active or 2. Inactive : "))
            update_student(student_list, Id, name_n, age_n, course_n, status_n)
        case 5:
            Id = input("Id to delete: ").strip()
            delete_student(student_list, Id)
        case 6:
            path = input("CSV save path (e.g. student.csv): ").strip()
            save_csv(student_list, path)
        case 7:
            path = input("CSV load path: ").strip()
            load_csv(path, student_list)
        case 8:
            print("Thank you for using the system. Goodbye!")
        case _:
            print("Invalid option.")