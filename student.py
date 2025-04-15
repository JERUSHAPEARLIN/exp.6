import csv
import os
import pickle

class StudentGradingSystem:
    def __init__(self, filename="students.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Marks", "Grade"])

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = list(map(float, input("Enter marks separated by space: ").split()))
        grade = self.calculate_grade(marks)

        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, name, marks, grade])
        print(f"Student {name} added with grade {grade}.\n")

    def calculate_grade(self, marks):
        avg = sum(marks) / len(marks)
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def display_students(self):
        print("\n--- All Students ---")
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        print("--------------------\n")

def main():
    system = StudentGradingSystem()

    while True:
        print("1. Add Student")
        print("2. View All Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.display_students()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()

