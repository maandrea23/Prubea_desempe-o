# CSV persistence module
import csv

def save_csv(student_list, path, include_header=True):
    # Saves inventory to CSV with validation
    if not student_list:
        print("student list empty, nothing to save.")
        return
    try:
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            if include_header:
                writer.writerow(['Id', 'name', 'age', 'course', 'status'])
            for p in student_list:
                writer.writerow([p['Id'], p['name'], p['age'], p['course'], p['status']])
        print(f"student list saved to: {path}")
    except PermissionError:
        print("Permission error to write file.")
    except Exception as e:
        print(f"Save error: {e}")

def load_csv(path, student_list):
    # Loads CSV with validations, overwrite or merge
    try:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        if not rows or rows[0] != ['Id', 'name', 'age', 'course', 'status']:
            print("Invalid header.")
            return "Header error."
        del rows[0]
        new_student = []
        errors = 0
        for row in rows:
            if len(row) != 5:
                errors += 1
                continue
            try:
                Id = int(row[0])
                name = (row[1])
                age = int(row[2])
                course = row[3]
                statu = int (row[4])

                new_student.append({ "Id": Id , "name": name, "age": age,"course": course,"status":statu})
            except ValueError:
                errors += 1
        print(f"Loaded {len(new_student)} valid products, {errors} invalid rows skipped.")
        action = input("Overwrite (O) or Merge (M)? ").upper().strip()
        if action == 'O':
            student_list[:] = new_student
            print(f"Overwritten with {len(new_student)} student.")
        else:
            for new_s in new_student:
                for existing in student_list:
                    if existing['Id'] == new_s['Id']:
                        if existing['name'].lower() == new_s['name'].lower():
                            if existing['age'] == new_s['age']:
                                if existing['course'] == new_s['course']:
                                    if existing['status'] == new_s['status']:
                                        print(f"Merged/updated {new_s['Id']}.")
                            break
                else:
                    student_list.append(new_s)
            print(f"Merged {len(new_student)} student.")
        return "Load complete."
    except FileNotFoundError:
        print("File not found.")
        return "File error."
    except UnicodeDecodeError:
        print("Encoding error in file.")
        return "Encoding error."
    except Exception as e:
        print(f"Generic error: {e}")
        return "Error."