# Student Management System

## Description
Application for managing student records. Supports CRUD operations (Create, Read, Update, Delete) and CSV persistence.

The system allows:
- Register new students.
- View student list.
- Search student by ID.
- Update student information.
- Delete students.

Each student includes:
- **ID** (unique identifier)
- **Name**
- **Age**
- **Course or program**
- **Status** (Active/Inactive)

## Features
- Interactive menu with 8 options.
- Input validation (positive numbers, non-empty strings).
- In-memory list with CSV persistence (save/load with merge/overwrite options).
- Error handling (file not found, permissions, encoding issues).

## Requirements
- Python 3.x (uses standard `csv` module)
- No external dependencies

## Installation
No installation required. Simply run the application from the project directory.

## File Structure
```
.
├── README.md             # This documentation
├── student.csv           # Data file (auto-generated)
└── src/
    ├── __init__.py      # (optional, not present)
    ├── main.py          # Entry point and main loop
    ├── menu.py          # Menu options list
    ├── validations.py   # Input validation and basic CRUD functions
    ├── services.py      # Menu option handlers
    └── persistencia.py  # CSV persistence (save/load)
```

## How to Use (Step-by-Step)

### 1. Run the Application
```bash
cd /home/Coder/Escritorio/Andrea_Ahumada_clan11/Prueba_Desempeño_Andrea_Ahumada
python src/main.py
```

### 2. Main Menu
```
1 - Add New Student
2 - Show All Students  
3 - Search a Student
4 - Update Student Info
5 - Delete Student
6 - Save CSV
7 - Load CSV
8 - Exit
Select option (1-8): 
```

### 3. Detailed Usage for Each Option

**1. Add New Student:**
```
ID: 1
Student name: John Doe
Age: 20
Course or program: Computer Science
1. Active or 2. Inactive: 1
```
→ Student added successfully.

**2. Show All Students:**
→ Displays formatted table:
```
Id: 1 | name: John Doe | age: 20 | course: Computer Science | status: Active
```

**3. Search a Student:**
```
ID to search: 1
```
→ Shows matching student or "Product not found."

**4. Update Student Info:**
```
Id to update: 1
New name: Jane Doe
New age: 21
New course: Data Science
New status, 1. Active or 2. Inactive: 1
```
→ Student updated.

**5. Delete Student:**
```
Id to delete: 1
```
→ Student deleted if found.

**6. Save CSV:**
```
CSV save path (e.g. student.csv): student.csv
```
→ Saves to specified path with header.

**7. Load CSV:**
```
CSV load path: student.csv
```
→ Loads data, prompts: Overwrite (O) or Merge (M)?

**8. Exit:**
→ "Thank you for using the system. Goodbye!"

### 4. CSV Format Example (student.csv)
```
Id,name,age,course,status
1,John Doe,20,Computer Science,Active
2,Jane Smith,22,Mathematics,Inactive
```

## Running the App
```bash
python src/main.py
```

**Quick Test Flow:**
1. Add 2 students (option 1)
2. Show list (option 2)
3. Save CSV (option 6 → student.csv)
4. Exit (8), restart app
5. Load CSV (option 7)
6. Verify list loaded correctly

## Known Issues / Notes
- Option 4 (Update) has bugs: updates wrong internal keys ('quantity' instead of 'age'/'course'/'status').
- Some comments reference "product/inventory" (from template).
- Search/Delete use string strip but ID is int - minor inconsistencies.

## Author
Andrea Ahumada 
