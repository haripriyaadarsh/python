with open("sample.txt",'r')as f:
	wordlist=f.read().split()
longword=len(max(wordlist,key=len))
result=[x for x in wordlist if len(x)==longword]
print(result)
f.close()