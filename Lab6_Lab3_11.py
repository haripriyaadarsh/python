import os
statinfo=os.stat("sample.txt")
print("File size of above file: ",statinfo.st_size)