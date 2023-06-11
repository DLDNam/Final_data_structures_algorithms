def compare_last_name(student1, student2):
    last_name1 = split_name(student1[1],1)
    last_name2 = split_name(student2[1],1)
    return 1 if last_name1 > last_name2 else -1 if last_name1 < last_name2 else 0
            
    