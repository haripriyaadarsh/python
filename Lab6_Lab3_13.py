with open("sample.txt",'a')as f1, open("my_test.txt",'r')as f2:
	for x in f2:
		f1.write(x)
f1.close()
f1=open("sample.txt",'r')
print(f1.read())