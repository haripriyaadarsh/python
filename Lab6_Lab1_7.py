def even(num_list):
	print(*filter(lambda x: x%2==0,num_list))
even([1,4,9,16,25,36,49,64,81,100])		