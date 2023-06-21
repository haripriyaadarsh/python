with open("my_test.txt",'r')as f:
	line=f.readlines()
	for x in line:
		print(x.rstrip('/n'))