count=0
with open("sample.txt",'r') as f:
	line=f.read().split()
count+=len(line)
print("Frequency of words in given file: ",count)