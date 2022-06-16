# poscount=0
# negcount=0
# pos=0
# neg=0
# while(True):
#     x=int(input("enter number:"))
#     if x==-1: break
#     elif x<-1:
#         negcount+=1
#         neg+=x
#     elif x>=0:
#         poscount+=1
#         pos+=x
# print(pos/poscount)
# print(neg/negcount)
# n=int(input("enter number:"))
# if n==0: print("enter valid number")
# else:
#     list1=[]
#     for i in range(1,n+1):
#         list1.append(i)
#     even_list=list(filter(lambda x: x%2==0, list1))
#     for x in even_list:
#         sq=list(map(lambda x:x**2, even_list))
#     print(sq)

# def invoice(n):
#     print("name\tage\tPrice")
#     for i in range(0,n):
#         print(details["name"][i]+"\t"+str(details["age"][i])+"\t"+str(details["cost"][i]))
#     print("Total:",details["total"])
#     print("12%\ttax\t"+str(details["tax"]))
#     tot=0
#     tot=details["total"]+details["tax"]
#     print("total=", tot)

# def calculate(n,r):
#     for i in range(0,n):
#         name=input("enter name:")
#         age=input("enter age:")
#         details["name"].append(name)
#         details["age"].append(age)
#         if r==1: details["cost"].append(350)
#         elif r==2: details["cost"].append(1500)
#         elif r==3: details["cost"].append(3000)
#         else: print("invalid")
#     for i in details["cost"]:
#         details["total"]+=float(i)
#     details["tax"]=details["total"]*0.12
#     invoice(n)

# details={"name":[], "age":[], "cost":[], "total":0, "tax":0}
# id=input("enter id:")
# password=input("enter password:")
# if id=="ABCD" and password=="WELCOME":
#     print("Continue for booking")
# else: print("enter valid credentials")
# print("1.Mumbai to Pune=350 per person")
# print("2.Mumbai to Goa=1500 per person")
# print("3.Mumbai to Bangalore=3000 per person")
# n=int(input("enter no of passengers:"))
# r=int(input("enter route no:"))
# calculate(n,r)

# def calculate(n):
#     q=int(input("enter quantity:"))
#     details["Quantity"].append(q)
#     if n==1 or n==3: temp=q*10
#     elif n==2: temp=q*15
#     details["price"].append(temp)

# def invoice(x):
#     print("name\t\tquantity\tprice")
#     for i in range(0,x):
#         print(str(details["name"][i])+"\t\t"+str(details["Quantity"][i])+"\t"+str(details["price"][i]))
#         details["total"]+=details["price"][i]
#     print("total", details["total"])

# details={"name":[],"Quantity":[],"price":[], "total":0}
# id=input("enter id:")
# password=input("enter password:")
# if id=="XYZ" and password=="bbb":
#     print("you can proceed and enter from menu:")
# else: print("invalid credentials")
# x=0
# n=1
# while(n>0):
#     n=int(input("enter option:"))
#     if n==0: 
#         break
#     else:
#         x+=1
#         if n==1: 
#             print("dairy milk-10rs per item")
#             details["name"].append("dairy milk")
#             calculate(n)
#             continue
#         elif n==2:
#             print("kitkat -15rs per item")
#             details["name"].append("kitkat")
#             calculate(n)
#             continue
#         elif n==3: 
#             print("snicker-10rs per item")
#             details["name"].append("snickers")
#             calculate(n)
#             continue
#         else: 
#             print("invalid")
#             x-=1
#             break
# invoice(x)