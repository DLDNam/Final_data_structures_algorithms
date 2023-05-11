import os
import matplotlib.pyplot as plt

class Student:
    def __init__(self, student_id, name, class_name, year_of_birth, gpa):
        self.student_id = student_id
        self.name = name
        self.class_name = class_name
        self.year_of_birth = year_of_birth
        self.gpa = gpa
    
    def __str__(self):
        return f"{self.student_id}, {self.name}, {self.class_name}, {self.year_of_birth}, {self.gpa}"
    
    def to_list(self):
        return [self.student_id, self.name, self.class_name, self.year_of_birth, self.gpa]

class StudentList:
    def __init__(self):
        self.student_list = []
    
    def read_file(self, filename):
        with open(filename, mode="r") as file_data:
            for row in file_data:
                row_list = row.strip().split(",")
                row_list[4] = float(row_list[4])
                student = Student(*row_list)
                self.student_list.append(student)
    
    def write_file(self, filename):
        with open(filename, mode="w") as file_data:
            for student in self.student_list:
                file_data.write(",".join(str(x) for x in student.to_list()) + "\n")
    
    def add_student(self):
        student_id = input("Student ID: ")
        name = input("Name: ")
        class_name = input("Class: ")
        year_of_birth = int(input("Year of birth: "))
        gpa = float(input("Grade point average: "))
        student = Student(student_id, name, class_name, year_of_birth, gpa)
        self.student_list.append(student)
        print("Added successfully")
    
    def display_students(self):
        print("\t\t\t+-----+----------+-----------------------+------------+-------------+-------*")
        print("\t\t\t|%-5s|%-10s|%-23s|%-12s|%-13s|%-7s|" %
              (" No ","Student_ID", "           Name", "   Class", "Year of birth", "  GPA"))
        print("\t\t\t+-----|----------+-----------------------+------------+-------------+-------|")
        for i, student in enumerate(self.student_list, start=1):
            print("\t\t\t|%-5s|%-10s|%-23s|%-12s|%-13s|%-7s|" %
                  (str(i), student.student_id, student.name, "  "+ student.class_name, "   " + str(student.year_of_birth), str(student.gpa)))
        print("\t\t\t+-----|---------+-----------------------+------------+-------------+-------*")
    
    def delete_student(self):
        student_id = input("Enter the student ID to remove from the list: ")
        filtered_list = [student for student in self.student_list if student.student_id != student_id]
        if len(filtered_list) == len(self.student_list):
            print("There is no student with that student ID")
        else:
            self.student_list = filtered_list
            print("Delete successfully")
    
    def search_by_name(self):
        name = input("Enter the name of the student you want to search for: ")
        filtered_list = [student for student in self.student_list if name.lower() in student.name.lower()]
        self.display_students(filtered_list)
    
    def search_by_student_id(self):
        student_id = input("Enter the Student_ID of the student you want to search for: ")
        filtered_list = [student for student in self.student_list if student.student_id == student_id]
        self.display_students(filtered_list)
    
    def search_by_gpa(self):
        gpa = float(input("Enter GPA you want to search for: "))
        filtered_list = [student for student in self.student_list if student.gpa == gpa]
        self.display_students(filtered_list)
    
    def search_by_class(self):
        class_name = input("Enter CLASS you want to search for: ")
        filtered_list = [student for student in self.student_list if student.class_name == class_name]
        filtered_list.sort(key=lambda student: student.name.split()[-1])
        self.display_students(filtered_list)
    
    def sort_by_gpa_ascending(self):
        self.student_list.sort(key=lambda student: student.gpa)
        self.display_students()
    
    def sort_by_gpa_descending(self):
        self.student_list.sort(key=lambda student: student.gpa, reverse=True)
        self.display_students()
    
    def sort_by_name(self):
        self.student_list.sort(key=lambda student: student.name.split()[-1])
        self.display_students()
    
    def generate_chart(self):
        class_names = sorted(set(student.class_name for student in self.student_list))
        class_averages = [sum(student.gpa for student in self.student_list if student.class_name == class_name) / 
                          len([student for student in self.student_list if student.class_name == class_name])
                          for class_name in class_names]
        plt.bar(x=class_names, height=class_averages, color='blue')
        plt.xlabel('Class', size=14)
        plt.ylabel('Average GPA', size=14)
        plt.grid(axis='y', linestyle='--')
        plt.gcf().set_size_inches(12, 6)
        plt.title('AVERAGE GPA BY CLASS', size=18)
        for i, class_name in enumerate(class_names):
            plt.annotate(f"{class_averages[i]:.2f}", xy=(class_name, class_averages[i]), ha='center', va='bottom')
        plt.show()
def display_menu():
    print("1. Add a student")
    print("2. Display the student list")
    print("3. Delete a student")
    print("4. Search for a student by name")
    print("5. Search for a student by Student_ID")
    print("6. Search for a student by GPA")
    print("7. Search for a student by Class")
    print("8. Sort the student list by GPA in ascending order")
    print("9. Sort the student list by GPA in descending order")
    print("10. Sort the student list by name")
    print("11. Generate a chart showing the average GPA by class")
    print("12. Save the student list to file")
    print("13. Quit")

def main():
    student_list = StudentList()
    filename = "students.txt"
    if os.path.isfile(filename):
        student_list.read_file(filename)
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            student_list.add_student()
        elif choice == "2":
            student_list.display_students()
        elif choice == "3":
            student_list.delete_student()
        elif choice == "4":
            student_list.search_by_name()
        elif choice == "5":
            student_list.search_by_student_id()
        elif choice == "6":
            student_list.search_by_gpa()
        elif choice == "7":
            student_list.search_by_class()
        elif choice == "8":
            student_list.sort_by_gpa_ascending()
        elif choice == "9":
            student_list.sort_by_gpa_descending()
        elif choice == "10":
            student_list.sort_by_name()
        elif choice == "11":
            student_list.generate_chart()
        elif choice == "12":
            student_list.write_file(filename)
            print("Saved successfully")
        elif choice == "13":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()