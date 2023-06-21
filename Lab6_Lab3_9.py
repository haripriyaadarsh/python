with open("sample.txt",'r') as f:
	line=len(f.readlines())	
print("No of lines in given file: ",line)	
f.close()
