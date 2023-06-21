my_str=input("Enter a string of your choice: ")
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str) :
	print("Given string is palindrome")
else :
	print("Given string is not palindrome")