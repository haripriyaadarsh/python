f=open("sample.txt","a")
f.write("\nThese are the 4 climates in Kerala")
f.close()
f=open("sample.txt","r")
print(f.read())
f.close()