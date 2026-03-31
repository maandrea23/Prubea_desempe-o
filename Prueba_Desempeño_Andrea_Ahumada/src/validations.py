
# Menu option validation
def getOption(options):
    while True:
        for i, option in enumerate(options, start=1):
            print(f"{i} - {option}")
        try:
            sel = int(input("Select option (1-8): "))
            if 1 <= sel <= 8:
                return sel
            print("Please choose 1-8.")
        except ValueError:
            print("Enter a valid number.")

# Input validation function
def inputValidator(type_input, msg, error_msg):
    user_input = input(msg)
    # Validate non-empty for str
    if type_input is str:
        if not user_input.strip():
            print(error_msg)
            return inputValidator(type_input, msg, error_msg)
    # Validate positive for numbers
    try:
        value = type_input(user_input)
        if type_input in (int, float) and value < 0:
            print(error_msg)
            return inputValidator(type_input, msg, error_msg)
        return value
    except ValueError:
        print(error_msg)
        return inputValidator(type_input, msg, error_msg)
    
def status():
    while True:
        try:
            st = int(input("1. Active or 2. Inactive "))
            if st ==1:
                return "Active" 
            if st == 2:
                return "Inactive"
            print("Must be 1 or 2")
        except ValueError:
            print("Must be a number")
    
def add_student(student_list, Id, name, age,course,statu):
    # Adds a product to the inventory
    students = {"Id": Id , "name": name, "age": age,"course": course,"status":statu}
    student_list.append(students)
    print(f"Student '{name}' added successfully.")

def show_student(student_list):
    # Shows inventory or indicates if empty
    if not student_list:
        print("List is empty.")
        return
    print("\n--- LIST ---")
    for p in student_list:
        print(f"Id: {p['Id']} | name: {p['name']} | age: {p['age']} | course: {p['course']} | status:{p['status']}")
    print("-----------------")

def search_student(student_list,Id):
    # Searches for product by ID returns dict or None
    for p in student_list:
        if p['Id'] == Id.strip():
            print(f"Found: {p['Id']} | name: {p['name']} | age: {p['age']} | course: {p['course']} | status:{p['status']}")
            return p
    print("Product not found.")
    return None

def update_student(student_list, Id, name_n=None, age_n=None, course_n=None, status_n=None):
    # Updates student by ID 
    p = search_student(student_list, Id)
    if p:
        if name_n is not None:
            p['name'] = name_n
        if age_n is not None:
            p['quantity'] = age_n
        if course_n is not None:
            p['quantity'] = course_n
        if status_n is not None:
            p['quantity'] = status_n

        print(f"Student '{Id}' updated.")

def delete_student(student_list, Id):
    # Deletes student by ID
    p = search_student(student_list, Id)
    if p:
        student_list.remove(p)
        print(f"Student '{Id}' deleted.")
