n=int(input("Enter a limit: "))
with open("sample.txt",'r') as f:
	lineList=f.readlines()
print("Following are the last n lines of a file: ")
for x in(lineList[-n:]):
	print(x,end='')
f.close()
