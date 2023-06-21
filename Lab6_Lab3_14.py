with open("sample.txt",'r')as f1, open("my_test.txt",'r') as f2:
	for line1,line2 in zip(f1,f2):
		print(line1+line2)