my_list=["hat","doll","pen","book","box"]
x=input("Enter an item to delete")
if x in my_list:
	my_list.remove(x)
	print(my_list)
else :
	print("enter another element")
print(my_list)