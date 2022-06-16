list_1 = input("Enter the contents of the list: ").split(",")
list_1 = list(set(list_1))
print(list_1)
a = input("Enter a string: ").lower()
dict1 = {}
if " " in a:
    a = a.replace("", "")
for m in range(len(a)):
 n = a.count(a[m])
 dict2 = {a[m] : n}
 dict1.update(dict2)
print(dict1)    
