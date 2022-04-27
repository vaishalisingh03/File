obj=open("students_list","w")
name=[]
for i in range(4):
    val=input("enter name:>")
    name.append(val+'\n')
obj.writelines(name)
obj.close()