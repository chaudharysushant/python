def student_info(student):
    name, age, grade = student
    print(f"Name : {name}")
    print(f"Age : {age}")
    print(f"Grade : {grade}")

def main ():
    student = {"Ram", 40, 3.8}
    print("student information:")
    student_info(student)

if __name__ == "__main__":
    main()