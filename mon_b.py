# n=input("enter number:")
# if "." in n:
#     x=n.split(".")
#     if x[0].isnumeric() and x[1].isnumeric():
#         print("before decimal point:",len(x[0]))
#         print("after decimal point:",len(x[1]))
#     else:
#         print("enter valid number!")
# else:
#     if n.isnumeric():
#         x=float(n)
#         x=str(x)
#         x=x.split(".")
#         print("before decimal point:",len(x[0]))
#         print("after decimal point:",len(x[1]))
#     else:
#         print("enter a valid number!")
# list1=[]
# for x in range(0,3):
#     a=input("enter side:")
#     if a.lstrip('-').isdigit() == True: 
#         a=int(a)
#         if a<=0:
#             a=input("enter greater than zero")
#             a=int(a)
#             list1.append(a)
#         else:
#             list1.append(a)
#     elif a.lstrip('-').isdigit() != True:
#         a=input("enter valid values")
#         a=int(a)
#         if a<=0:
#             a=input("enter greater than zero")
#             a=int(a)
#             list1.append(a)
#         else:
#             list1.append(a)
# a=list1[0]
# b=list1[1]
# c=list1[2]
# if (a or b or c) == 0:
#     print("non zero value")
# if (a+b>c and a+c>b and b+c>a) ==True:
#     if a==b and a==c: print("equilateral triangle")
#     elif a==b or a==c: print("isoseles triangle")
#     else: print("scalene triangle")
# else:
#     print("does not form a triangle")
# import re
# my_input=input("enter position:")
# if my_input.isalnum():
#     if len(my_input)>2: print("enter valid position")
#     else:
#         a = re.search(r"[A-H][1-8]", my_input)
#         b = re.search(r"[1-8][A-H]", my_input)
#         if a or b:
#             x = re.findall(r"[BDFH][2468]", my_input)
#             y = re.findall(r"[BDFH][1357]", my_input)
#             i = re.findall(r"[ACEG][1357]", my_input)
#             j = re.findall(r"[ACEG][2468]", my_input)
#             if x: print("belongs to black square")
#             elif y: print("belongs to white square")
#             elif i: print("belongs to black square")
#             elif j: print("belongs to white square")
#         else: print("enter valid position")
# else: print("enter valid position")
# import re
# my_pass=input("enter passwords:").split(",")
# result = []
# for x in range(0,len(my_pass)):
#     y=len(my_pass[x])
#     if (y<15 and y>8) !=True:
#         pass
#     else:
#         a=re.findall(r"[a-z]+", my_pass[x])
#         b=re.findall(r"[0-9]+", my_pass[x])
#         c=re.findall(r"[A-Z]+", my_pass[x])
#         d=re.findall(r"[#$@]+", my_pass[x])
#         if (a and b and c and d):
#             result.append(my_pass[x])
# res=",".join(result)
# print(res)