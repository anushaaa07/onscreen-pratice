print("Input lengths of the triangle sides- ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
	print("It is an equilateral triangle")
elif a==b or b==c or c==a:
	print("It is an isosceles triangle")
else:
	print("It is a scalene triangle")
