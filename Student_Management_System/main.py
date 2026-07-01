import os

print("Current Folder:", os.getcwd())


def menu():
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Total Students")
    print("7. Exit")
    print("=" * 45)


while True:

    menu()

    choice = input("Enter your choice: ")

    # ---------------- ADD ----------------
    if choice == "1":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        branch = input("Enter Branch: ")

        with open("students.txt", "a") as file:
            file.write(f"{name},{age},{branch}\n")

        print("\nStudent Added Successfully!")

    # ---------------- VIEW ----------------
    elif choice == "2":

        try:
            with open("students.txt", "r") as file:

                students = file.readlines()

                if not students:
                    print("\nNo Students Found.")
                else:
                    print("\n------ STUDENT LIST ------")

                    for student in students:
                        data = student.strip().split(",")

                        if len(data) == 3:
                            print("-" * 30)
                            print("Name   :", data[0])
                            print("Age    :", data[1])
                            print("Branch :", data[2])

        except FileNotFoundError:
            print("Student file not found.")

    # ---------------- SEARCH ----------------
    elif choice == "3":

        search = input("Enter Student Name: ").lower()

        found = False

        try:
            with open("students.txt", "r") as file:

                for student in file:

                    data = student.strip().split(",")

                    if len(data) == 3 and data[0].lower() == search:

                        print("\nStudent Found")
                        print("-" * 20)
                        print("Name   :", data[0])
                        print("Age    :", data[1])
                        print("Branch :", data[2])

                        found = True

                if not found:
                    print("Student Not Found.")

        except FileNotFoundError:
            print("Student file not found.")

    # ---------------- DELETE ----------------
    elif choice == "4":

        delete_name = input("Enter Student Name: ").lower()

        students = []

        deleted = False

        try:

            with open("students.txt", "r") as file:

                for student in file:

                    data = student.strip().split(",")

                    if len(data) == 3 and data[0].lower() != delete_name:
                        students.append(student)
                    elif len(data) == 3:
                        deleted = True

            with open("students.txt", "w") as file:
                file.writelines(students)

            if deleted:
                print("Student Deleted Successfully.")
            else:
                print("Student Not Found.")

        except FileNotFoundError:
            print("Student file not found.")

    # ---------------- UPDATE ----------------
    elif choice == "5":

        update_name = input("Enter Student Name: ").lower()

        students = []

        updated = False

        try:

            with open("students.txt", "r") as file:

                for student in file:

                    data = student.strip().split(",")

                    if len(data) == 3 and data[0].lower() == update_name:

                        print("\nEnter New Details")

                        new_name = input("Name: ")
                        new_age = input("Age: ")
                        new_branch = input("Branch: ")

                        students.append(f"{new_name},{new_age},{new_branch}\n")

                        updated = True

                    else:
                        students.append(student)

            with open("students.txt", "w") as file:
                file.writelines(students)

            if updated:
                print("Student Updated Successfully.")
            else:
                print("Student Not Found.")

        except FileNotFoundError:
            print("Student file not found.")

    # ---------------- COUNT ----------------
    elif choice == "6":

        try:
            with open("students.txt", "r") as file:

                total = len(file.readlines())

                print(f"\nTotal Students: {total}")

        except FileNotFoundError:
            print("Student file not found.")

    # ---------------- EXIT ----------------
    elif choice == "7":

        print("\nThank You!")
        break

    else:

        print("Invalid Choice. Please try again.")