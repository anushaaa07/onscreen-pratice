# import re
# list_1=[]
# list=["city","toy","potato"]
# for x in list:
#     a=re.findall("y$", x)
#     if a:
#         str=x[0:len(x)-1]
#         b=re.findall("t$",str)
#         if b:
#             new=str+"ies"
#             list_1.append(new)
#         else:
#             new=x+"s"
#             list_1.append(new)
#     else:
#         new=x+"es"
#         list_1.append(new)
# result=", ".join(list_1)
# print(result)

# x = input("Enter a number: ")
# for i in x:
#     print("*"*int(i))

# def rev_number(n):
#   s = 0
#   while True:
#     k = str(n)
#     if k == k[::-1]:
#       break
#     else:
#       m = int(k[::-1])
#       n += m
#       s += 1
#   return n 

# print(rev_number(1234))
# print(rev_number(1473))