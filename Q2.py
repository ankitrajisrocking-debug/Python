def fib_rec(n):
	if n<= 0:
		return 0
	elif n== 1:
		return 1
	else:
		return fib_rec(n-1)+ fib_rec(n-2)
		
def fib_ser(count):
	series= []
	for i in range(count):
		series.append(fib_rec(i))
	return series
	
# example test run

count= 10
print(f"Fibonacci series upto {count} terms: ")
print(fib_ser(count))
