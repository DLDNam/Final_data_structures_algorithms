def quicksort_sv(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        less = [sv for sv in data[1:] if sv[1] > pivot[1]]
        greater = [sv for sv in data[1:] if sv[1] <= pivot[1]]
        return quicksort_sv(greater) + [pivot] + quicksort_sv(less)
    
stack_sv = []

stack_sv.append(("Nguyen Van A", 8.5,"Ha Noi"))
stack_sv.append(("Tran Thi B", 7.2,"Tuyen Quang"))
stack_sv.append(("Le Quoc C", 9.0, "Hai Duong"))
stack_sv.append(("Le Quoc D", 5.0, "Da Nang"))
stack_sv.append(("Dinh Van Nam", 7.6, "Nam Dinh"))

stack_sv = quicksort_sv(stack_sv)
print("Danh sách sinh viên theo điểm trung bình:")
for sv in stack_sv:
    print(sv[0], "-", sv[1], "-", sv[2])