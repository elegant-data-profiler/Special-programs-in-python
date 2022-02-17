class raider:
	def __init__(self,a):
		self.a=a
	def bike(self,a):
		print('raiding')
	def bike(self,a):
		print("bike raiding")
class copper:
	def __init__(self,a):
		self.a=a
	def bike(self,a):
		print("High speed")
class driver(raider,copper):
	def __init__(self,a):
		self.a=a
	def car(self):
		print("car driving")
r=driver("one")
print(r.bike(1))
print(r.car())
