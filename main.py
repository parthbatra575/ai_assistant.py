class Student:
    def __init__(self, name):
        self.name = name
        self.score = 0


def science_quiz(student):
    questions = [
        ("What planet is known as the Red Planet?", "mars"),
        ("What gas do plants absorb from the atmosphere?", "carbon dioxide"),
        ("How many bones are in the adult human body?", "206")
    ]

    for question, answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == answer:
            print("Correct!")
            student.score += 1
        else:
            print("Wrong! Correct answer:", answer)


def maths_quiz(student):
    questions = [
        ("5 + 7 =", "12"),
        ("9 x 6 =", "54"),
        ("Square root of 81 =", "9")
    ]

    for question, answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == answer:
            print("Correct!")
            student.score += 1
        else:
            print("Wrong! Correct answer:", answer)


def view_score(student):
    print(f"\n{student.name}'s Score: {student.score}")


name = input("Enter your name: ")
student = Student(name)

while True:
    print("\n===== AI Study Assistant =====")
    print("1. Science Quiz")
    print("2. Maths Quiz")
    print("3. View Score")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        science_quiz(student)

    elif choice == "2":
        maths_quiz(student)

    elif choice == "3":
        view_score(student)

    elif choice == "4":
        print("Thank you for using AI Study Assistant!")
        break

    else:
        print("Invalid choice. Please try again.")
