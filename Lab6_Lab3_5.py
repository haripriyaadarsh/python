def file_read(fname):
	with open(fname) as f:
		contents=f.readlines()
		content_list=list(contents)
		print(content_list)
file_read("line.txt")