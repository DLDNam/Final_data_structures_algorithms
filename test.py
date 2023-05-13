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

print(student_list[1][1])