terms = []

def fib(val1, val2):
	val = val1 + val2
	if val > 4000000:
		return
	if (val) % 2 == 0:
		terms.append(val)

	return fib(val2, val)

fib(1, 1)

print sum(terms)

#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
