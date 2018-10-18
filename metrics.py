def d_1(x,y):
	return (x - y) ** 2

def d_2(x, y):
	return abs(x-y) ** (1 / 2)

def d_3(x, y):
	return (abs(x - y) / (1 + abs(x - y)))

def test(func):
	for i in range(-1000,1000):
		for j in range(-1000, 1000):
			for k in range(-1000, 1000):
				if func(i/100.0, j/100.0) > func(i/10.0, k/10.0) + func(j/10.0, k/10.0):
					return func, "fails for", [i/100.0,j/100.0 ,k/100.0]

	return func, " works"
print test(d_1)
print test(d_2)
print test(d_3)
