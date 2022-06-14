import re
my_pass=input("enter password: ").split(",")
result = []
for x in range(0,len(my_pass)):
    y=len(my_pass[x])
    if (y<15 and y>8) !=True:
        pass
    else:
        a=re.findall(r"[a-z]+", my_pass[x])
        b=re.findall(r"[0-9]+", my_pass[x])
        c=re.findall(r"[A-Z]+", my_pass[x])
        d=re.findall(r"[#$@]+", my_pass[x])
        if (a and b and c and d):
            result.append(my_pass[x])
res=",".join(result)
print(res)

