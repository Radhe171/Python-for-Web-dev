students = [("Rahul", 85), ("Priya", 92), ("Amit", 78)]

students.append(("Neha", 88))   # list: add a new student

for name, marks in students:    # tuple: unpack each record
    print(name, "scored", marks)