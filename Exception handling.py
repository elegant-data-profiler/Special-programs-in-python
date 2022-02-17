def sample(a,b):
	print('hiiii')
	try:
		c=((a+b)/(a-b))
	except zerodivisionError:
		print("a/b result in 0")
	else:
		print(c)
sample(2.0,3.0)