input_list = input("Enter the elements of the list separated by space : ")
mylist = input_list.split()
print("The entered list is : \n", "List :", mylist)
# convert into int
for i in range(len(mylist)):
    mylist[i] = int(mylist[i])
print("The positive terms in list is :\n")
for x in mylist:
    if x > 0:
        print(x, end=" ")
