def add_student(students):

    print("Enter student name: ")
    name = input().strip()
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists.")
            return
    new_student = {"name": name, "grades": []}
    students.append(new_student)

def add_grades(students):
    if not students:
        print("List of students is empty")
        return

    print("Enter student name: ")
    name = input().strip()

    for student in students:
        if student["name"].lower() == name.lower():
            while True:
                print("Enter a grade (or 'done' to finish): ")
                grade_input = input().strip()

                if grade_input.lower() == 'done':
                    break

                try:
                    grade = float(grade_input)
                    if 0 <= grade <= 100:
                        student["grades"].append(grade)
                    else:
                        print("Invalid grade.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            return

    print(f"Student '{name}' not found.")





def show_report(students):
    if not students:
        print("List of students is empty")
        return

    print("\n--- Student Report ---")

    averages = []

    for student in students:
        name = student["name"]
        grades = student["grades"]

        try:
            if grades:
                average = sum(grades) / len(grades)
                averages.append(average)
                print(f"{name}'s average grade is {average:.1f}.")
            else:
                print(f"{name}'s average grade is N/A.")
        except ZeroDivisionError:
            print(f"{name}'s average grade is N/A.")

    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)

        print("---")
        print(f"Max Average: {max_avg:.1f}")
        print(f"Min Average: {min_avg:.1f}")
        print(f"Overall Average: {overall_avg:.1f}")
    else:
        print("No grades available.")


def find_top_performer(students):
    if not students:
        print("List of students is empty.")
        return
    students_with_grades = [student for student in students if student["grades"]]

    if not students_with_grades:
        print("No students with grades available.")
        return

    try:
        top_student = max(students_with_grades,
                          key=lambda student: sum(student["grades"]) / len(student["grades"]))

        top_avg = sum(top_student["grades"]) / len(top_student["grades"])
        print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.1f}.")

    except Exception as e:
        print(f"Error finding top performer: {e}")

def main():
    students = []
    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                add_student(students)
            elif choice == "2":
                add_grades(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()