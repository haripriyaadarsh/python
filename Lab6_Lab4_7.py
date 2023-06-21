k=int(input("Enter a limit : "))
def sum_num(n):
	if n<1 :
		return 0
	else :
		return n+sum_num(n-2)
print(sum_num(k))
print(sum_num(10))