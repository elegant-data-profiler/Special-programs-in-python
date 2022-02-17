a=3
b=2

try:
	print("open program")
	print(a/b)
	k=int(int("enter a num"))
	print(k)
except ZeroDivisionError as e:
	print("zeroDivisionError",e)
except ValueError as e:
	print("invalid")
except Excepton as e:
	print("somthing")
finally:
	print("close the program")