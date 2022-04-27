xyz=open("people1.text","w")
for i in range(31):
    name=input("enter name:>")
    xyz.write(name)
    xyz.write("\n")
xyz.close()
