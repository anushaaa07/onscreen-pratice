l = input("Enter the length: ")
b = input("Enter the breadth: ")
h = input("Enter the breadth: ")
unit = input("Enter unit: ")
if (l.strip("-").isnumeric() and b.strip("-").isnumeric() and h.strip("-").isnumeric()) is False:
 print ("Please try again by using positive numeric values instead of strings. ")
else:
 l=float(l)
 b=float(b)
 h=float(h)
if l<=0 or b<=0 or h<=0:
    print("Please try again by using positive numeric values instead of negative ones or zero. ") 
else:
     v = l * b * h
     d = ((l**2) + (b**2) + (h**2)) ** (0.5)
print("The volume of is", v, "cubic", unit)
print("The diagonal is", d, unit)
       

