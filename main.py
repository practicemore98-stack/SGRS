import csv
import os

FILE_NAME = "grievances.csv"


# Initialize file
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file_write:
            csv_writer = csv.writer(file_write)
            csv_writer.writerow(["ID", "Name", "Category", "Description", "Status"])


# Generate unique ID
def generate_id():
    with open(FILE_NAME, "r") as file_read:
        data = list(csv.reader(file_read))
        return str(len(data))


# Submit grievance
def submit_grievance():
    print("\n--- Submit Grievance ---")
    name = input("Enter your name: ")
    category = input("Enter category (Academic/Hostel/Exam/etc): ")
    description = input("Enter grievance description: ")

    grievance_id = generate_id()

    with open(FILE_NAME, "a", newline="") as file_append:
        csv_writer = csv.writer(file_append)
        csv_writer.writerow([grievance_id, name, category, description, "Submitted"])

    print(f"\nGrievance submitted successfully! Your ID is: {grievance_id}\n")


# Check status
def check_status():
    print("\n--- Check Grievance Status ---")
    search_id = input("Enter your Grievance ID: ")

    found = False

    with open(FILE_NAME, "r") as file_read:
        csv_reader = csv.reader(file_read)
        next(csv_reader)

        for row in csv_reader:
            if row[0] == search_id:
                print("\nGrievance Found:")
                print("ID:", row[0])
                print("Name:", row[1])
                print("Category:", row[2])
                print("Description:", row[3])
                print("Status:", row[4])
                found = True
                break

    if not found:
        print("Grievance ID not found!\n")


# Admin update
def admin_update():
    print("\n--- Admin Update ---")
    search_id = input("Enter Grievance ID to update: ")

    updated = False

    with open(FILE_NAME, "r") as file_read:
        rows = list(csv.reader(file_read))

    for i in range(1, len(rows)):
        if rows[i][0] == search_id:
            print("Current Status:", rows[i][4])
            new_status = input("Enter new status (Under Review/In Process/Resolved/Rejected): ")
            rows[i][4] = new_status
            updated = True
            break

    if updated:
        with open(FILE_NAME, "w", newline="") as file_write:
            csv_writer = csv.writer(file_write)
            csv_writer.writerows(rows)
        print("Status updated successfully!\n")
    else:
        print("Grievance ID not found!\n")


# View all grievances
def view_all():
    print("\n--- All Grievances ---")
    with open(FILE_NAME, "r") as file_read:
        csv_reader = csv.reader(file_read)
        for row in csv_reader:
            print(row)


# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== Student Grievance Redressal System =====")
        print("1. Submit Grievance")
        print("2. Check Status")
        print("3. Admin Update")
        print("4. View All (Admin)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            submit_grievance()
        elif choice == "2":
            check_status()
        elif choice == "3":
            admin_update()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Thank you for using SGRS!")
            break
        else:
            print("Invalid choice! Try again.")


# IMPORTANT (this was your issue)
if __name__ == "__main__":
    main()
