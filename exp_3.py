prime = []
composite = []
num = int(input("Enter a number: "))
while num > 1 or num == -1:
    flag = False
    if num==-1:
        p_list=len(prime)
        c_list=len(composite)
        print("Number of prime numbers are: ", p_list, "Number of composite numbers are: ", c_list)
        break
    for i in range(2, num):
        if (num % i) == 0:
            flag == True
    if flag ==True:
         composite.append(num)
    else:
         prime.append(num)
    num = int(input("Enter a number: "))           
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    n =  temp % 10
    temp = temp // 10
    sum = sum + pow(n, order)
if (sum == num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")       