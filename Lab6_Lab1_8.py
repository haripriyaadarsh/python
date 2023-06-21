import random
n=random.randrange(1,10)
trial=int(input("Enter a number :"))
while n!= trial :
	if trial < n:
		print("too low")
		trial=int(input("Enter number again :"))
	elif trial>n :
		print("too high")
		trial=int(input("Enter number again :"))
	else:
		break
print("you guessed correctly")