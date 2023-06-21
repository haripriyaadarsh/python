name=input("Enter your name:\n")
age=int(input("Enter your age: \n"))
if age<100 :		
		year=2023+(100-age)
		print("Greetings %s !!! you will turn 100 years old in the year %d" %(name,year))
elif age==100 :
		print("Greetings %s !!! you are 100 years old" %(name))
else :
		print("Greetings %s !!! you are above 100 years" %(name))