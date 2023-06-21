n=int(input("Enter a limit: "))
with open("sample.txt",'r') as f:
	lineList=f.readlines()
print("following are the 1st n lines of the file")
for x in(lineList[ :n]):
	print(x,end='')
f.close()
