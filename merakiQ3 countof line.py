xyz=open("students_list","r")
count_line=0
for i in xyz:
    count_line+=1
print(count_line)
xyz.close()