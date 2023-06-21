my_list=["abc","klm","ghi"]
with open("sample.txt",'a') as f:
	f.write(','.join(my_list))
f.close()
f=open("sample.txt",'r')
print(f.readlines())
