import random
import array
max_len=12
digits=['0','1','2','3','4','5','6','7','8','9']
lo_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['@','/','#','!','$','%','^','&','*','|','?','.','<','>','~','(',')','=',':',';']
final_list=digits+lo_case+up_case+symbols
rand_dg=random.choice(digits)
rand_lo=random.choice(lo_case)
rand_up=random.choice(up_case)
rand_sym=random.choice(symbols)
temp_pass=rand_dg+rand_lo+rand_up+rand_sym
for x in range(max_len-4):
	temp_pass=temp_pass+random.choice(final_list)
temp_pass_list=array.array('u',temp_pass)
random.shuffle(temp_pass_list)
password=" "
for x in temp_pass_list:
	password=password+x
print(password)