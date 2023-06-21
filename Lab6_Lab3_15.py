import random
with open("my_test.txt",'r')as f:
	line=f.read().splitlines()
print(random.choice(line))