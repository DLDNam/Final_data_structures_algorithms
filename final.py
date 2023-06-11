# Student Management System
# Nember: Dinh Le Duc Nam, Dinh Quang Tung
# Topic Idea: 
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

student_list = []

#Chuan hao xau
def CHX(st):
    st = st.title()
    st = st.strip()
    kt = "  "
    while kt in st:
        st = st.replace("  "," ")
    return st


# dọc file
file_data = open("Datastudent.txt", mode="r")
while (1 != 2):
    row = file_data.readline()
    if row == "":
        break
    row_list = row.strip().split(",")
    row_list[4] = float(row_list[4])
    student_list.append([row_list[0], CHX(row_list[1]), row_list[2], row_list[3], row_list[4]])

# Ghi ra file
def write_file():
    with open('Datastudent.txt', 'w') as file_data:
        for sv in student_list:
            file_data.write(str(sv[0]) + "," + str(CHX(sv[1])) + "," +
                            str(sv[2]) + "," + str(sv[3]) + "," + str(sv[4]) + "\n")


def menu():
    print("1: ADD")
    print("2: THE DISPLAY ALL OF STUDENTS")
    print("3: DELETE")
    print("4: UPDATE")
    print("5: SEARCH")
    print("6: SORT")
    print("7: CHART OF AVERAGE GPA BY CLASS")
    print("8: EXIT")

# Them Sinh Vien
def add_student():
    student_id = str(input("Student ID: "))
    name = str(input("Name: "))
    Class = str(input("Class: "))
    year_brith = int(input("Year of birh: "))
    GPA = float(input("Grade point average: "))
    student_list.append([student_id, CHX(name), Class, year_brith.strip(), GPA])

# Display all of students
def display_students(stack):
    print("\t\t\t+-----+----------+-----------------------+------------+-------------+-------*")
    print("\t\t\t|%-5s|%-10s|%-23s|%-12s|%-13s|%-7s|" %
          (" No ","Student_ID", "           Name", "   Class", "Year of birth", "  GPA"))
    print("\t\t\t+-----|----------+-----------------------+------------+-------------+-------|")
    stt = 0
    for sv in stack:
        stt +=1
        print("\t\t\t|%-5s|%-10s|%-23s|%-12s|%-13s|%-7s|" %
              (str(stt),sv[0], sv[1], "  "+ sv[2], "   " + sv[3], str(sv[4])))
    print("\t\t\t+-----|---------+-----------------------+------------+-------------+-------*")

# DELETE
def Delete(data, ID):
    filter = [sv for sv in data if sv[0] != ID]
    return filter

# search by name
def search_name(name, st):
    name = name.lower()
    st = st.lower()
    if name in st:
        return True
    else:
        return False

def search_GPA(data, p):
    tam = []
    for sv in data:
        if sv[4] == p:
            tam.append(sv)
    return tam

# Thuat toan sap xep
def quicksort_up(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        right = [sv for sv in data[1:] if sv[4] > pivot[4]]
        left = [sv for sv in data[1:] if sv[4] <= pivot[4]]
        return quicksort_up(left) + [pivot] + quicksort_up(right)

def quicksort_down(data):
    if len(data) <= 1:
        return data
    else:     
        pivot = data[0]
        less = [sv for sv in data[1:] if sv[4] < pivot[4]]
        greater = [sv for sv in data[1:] if sv[4] >= pivot[4]]
        return quicksort_down(greater) + [pivot] + quicksort_down(less)

# vẽ biểu đồ
def subclass(data):
    lop = []
    for cl in data:
        if cl[2] not in lop:
            lop.append(cl[2])
    return lop


def AVG_GPA(data, Class):
    mean = [0 for i in range(len(Class))]
    dem = [0 for i in range(len(Class))]
    for point in data:
        for i in range(len(Class)):
            if point[2] == Class[i]:
                dem[i] = dem[i] + 1
                mean[i] = mean[i] + point[4]
                break
    for i in range(len(mean)):
        mean[i] = round(mean[i]/dem[i], 2)
    return mean

def sort(x, y):
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
                y[i], y[j] = y[j], y[i]

def SHOW(X, Y):
    plt.bar(x=X, height=Y, color='blue')
    plt.xlabel('Class', size=14)
    plt.xticks(rotation = 5)
    plt.ylabel('Average GPA', size=14)
    plt.grid(axis='y', linestyle='--')
    plt.gcf().set_size_inches(12, 6)
    plt.title('AVERAGE GPA BY CLASS', size=18)
    for i in range(len(X)):
        plt.annotate((Y[i]), xy=(X[i], (Y[i])), ha='center', va='bottom')
    plt.show()


# MAIN PROGAMING
while (1 != 0):
    os.system('cls')
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
        input("Added successfully")

    elif choice == 2:
        display_students(student_list)
        input("ENTER")

    elif choice == 3:
        os.system("cls")
        std_ID = input("Enter the student ID to remove from the list: ")
        kt = len(student_list)
        student_list = Delete(student_list, std_ID)
        if kt == len(student_list):
            input("There is no student with that student ID")
        else:
            input("Delete successfully")
    
    elif choice == 5:
        while (1 != 0):
            os.system('cls')
            print("1: Search by name")
            print("2: search by Student ID")
            print("3: Search by GPA")
            print("4: Search by class")
            print("5: EXIT")
            pick = int(input("Enter choice: "))
            if pick == 1:
                os.system('cls')
                name = input("Enter the name of the student you want to search for: ")
                name = CHX(name)
                filtered_list = filter(lambda x: search_name(name, x[1]) == True, student_list)
                display_students(filtered_list)
                input("ENTER")
            
            elif pick == 2:
                os.system("cls")
                ID = input("Enter the Student_ID of the student you want to search for: ").strip()
                filtered_list = filter(lambda x: x[0] == ID, student_list)
                display_students(filtered_list)
                input("ENTER")
            
            elif pick == 3:
                os.system("cls")
                Point = float(input("Enter GPA you want to search for: "))
                filtered_list = search_GPA(student_list, Point)
                print(display_students(filtered_list))
                input("ENTER")
            
            elif pick == 4:
                os.system("cls")
                cl = input("Enter CLASS you want to search for: ").strip()
                filtered_list = filter(lambda x: x[2] == cl, student_list)
                filtered_list = list(filtered_list)
                display_students(filtered_list)
                input("ENTER")
            
            elif pick == 5:
                break

    elif choice == 6:
        while (1 != 0):
            os.system("cls")
            print("1: Sort by increasing GPA")
            print("2: Sort by decreasing GPA")
            print("3: EXIT")
            pick = int(input("Enter choice: "))
            if pick == 1:
                student_list = quicksort_up(student_list)
                display_students(student_list)
                input("ENTER")
            
            elif pick == 2:
                student_list = quicksort_down(student_list)
                display_students(student_list)
                input("ENTER")
            elif pick == 3:
                break

    elif choice == 7:
        Class = subclass(student_list)
        Average_point = AVG_GPA(student_list, Class)
        sort(Average_point,Class)
        SHOW(Class, Average_point)

    elif choice == 8:
        write_file()
        break
