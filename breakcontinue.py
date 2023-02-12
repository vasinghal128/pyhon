students = ["ram", "shyam", "kishna", "radha", "radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

    for student in students:
        if student == "radha":
            continue;
        print(student)
