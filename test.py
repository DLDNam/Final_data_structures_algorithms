def Nhap_danh_sach_ten():
    """
    :return: List of name is string
    """
    list_name = []
    n = int(input("Nhap vao so luong ten: n = "))
    print("Nhap vao danh sach cac ten:")
    for i in range(n):
        print("\tSo thu tu ", i+1, ":", sep="", end=" ")
        list_name.append(input())

    return list_name


def Sap_xep_Abc(lst):
    """
    :param lst: list of name is string
    :return: void
    """
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


# Chuong trinh chinh
lst = Nhap_danh_sach_ten()

# Hien thi
print("Danh sach vua nhap la:")
for i in range(len(lst)):
    print("\t", lst[i], end=" ")

# Sap xep tang dan
Sap_xep_Abc(lst)

print("\nDanh sach sau khi sap xep la:")
for i in range(len(lst)):
    print("\t", lst[i], end=" ")