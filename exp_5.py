# def my_function(fname, lname):
#  print(fname + " " + lname)
# my_function("Amit", "Kumar")
# def my_function(*kids):
#  print("The youngest child is " + kids[0])
# my_function("Emil", "Tobias", "Linus")
# def my_function(college3, college2, college1):
#  print("The Best college is " + college1)
# my_function('KJSCE','BITS ','IIT')
# def my_function(country= "Sri Lanka"):
#  print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# def tri_recursion(k):
#  if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#  else:
#         result = 0
#  return result
# print("Recursion Example Results")
# tri_recursion(7)
# print((lambda x: x*2) (10))
# twice = lambda x: x*2
# print(twice(7))
# def palindrome(str):
#  if len(str) == 1:
#   return True
#  elif len(str) == 2:
#   if str[0] == str[1]:
#    return True
#   else:
#    return False
#  elif str[0] == str[-1]:
#   return palindrome(str[1:-1])
#  else:
#   return False
# if palindrome(input()):
#  print("It is a Palindrome")
# else:
#  print('It is not a Palindrome')
x=list(map(int,input().split()))
even=[]
odd=[]
o=lambda y: y%2==1
odd=filter(o,x)
print("List of odd numbers: ", list(odd))
e=lambda y: y%2==0
even=filter(e,x)
print("List of even numbers: ", list(even))


