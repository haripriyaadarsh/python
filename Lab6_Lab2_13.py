my_list=['a',['bb','ee','ff'],'g',['hh','iii'],'j']
flat_list=[num for sublist in my_list for num in sublist]
print(flat_list)