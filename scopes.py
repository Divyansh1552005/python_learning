x = 5

def func():
	global x
	x = 12
	
func()
print(x) # output - 12