import os
import matplotlib as mpl
import matplotlib.pyplot as plt

stack_std = []
i = 1

#dọc file 
file_data = open("Datastudent.txt", mode="r")
while (1 != 2):
    row = file_data.readline()
    if row == "":
        break
    row_list = row.split(",")
    row_list[4] = float(row_list[4])
    stack_std.append([row_list[0], row_list[1], row_list[2], row_list[3], row_list[4]])

def Delete(data,ID):
    filter = [sv for sv in data if sv[0]!=ID]
    return filter

i = "21070878"
stack_std = Delete(stack_std,i)
for sv in stack_std:
    print (sv)