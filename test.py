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

def split_name(name,n):
    name = str(name.lower())
    last_name = name.split(" ")
    return last_name[n]


def sort_name(data, compare_func):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = []
        equal = []
        greater = []
        for element in data:
            if compare_func(element, pivot) < 0:
                less.append(element)
            elif compare_func(element, pivot) == 0:
                equal.append(element)
            else:
                greater.append(element)
        return sort_name(less, compare_func) + equal + sort_name(greater, compare_func)

def compare_last_name(student1, student2):
    if student1[1] == student2[1]:
        return 0
    name1 = split_name(student1[1],-1)
    name2 = split_name(student2[1],-1)
    if name1 > name2:
        return 1
    elif name2 < name1:
        return -1
    space = 0
    num_space1 = student1[1].count(" ")
    num_space2 = student2[1].count(" ")
    while (space < num_space1) and (space < num_space2):
        name1 = split_name(student1[1],space)
        name2 = split_name(student2[1],space)
        if name1 > name2:
            return 1
        elif name1 < name2:
            return -1
        else:
            space = space + 1
    return 0
            
    

student_list = sort_name(student_list,compare_last_name)
print(display_students(student_list))