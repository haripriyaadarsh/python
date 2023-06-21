my_array=[]
with open("sample.txt",'r') as f:
	for x in f:
		my_array.append(x)
	print(my_array)
f.close()