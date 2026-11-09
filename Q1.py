def factorial(n):
	if n< 0:
		return None # undefined
	result= 1
	for i in range(2, n+1):
		result= result* i
	return result
	
def is_prime(n):
	if n< 2:
		return False
	for i in range(2, int(n** 0.5)+ 1):
		if n% i ==0:
			return False
		return True
		
		
num= 7
print(f"Factorial of {num} is {factorial(num)}")
print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
