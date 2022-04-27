banks_list=["Kotak","HDFC","RBL","SBI","Bank of Baroda"]
obj=open("banks.txt","w")
for i in banks_list:
    obj.write(i)
    obj.write('\n')
    print(i)
obj.close()