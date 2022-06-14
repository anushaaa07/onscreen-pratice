import re
my_input=input("enter position:")
if my_input.isalnum():
    if len(my_input)>2: print("enter valid position")
    else:
        a = re.search(r"[A-H][1-8]", my_input)
        b = re.search(r"[1-8][A-H]", my_input)
        if a or b:
            x = re.findall(r"[BDFH][2468]", my_input)
            y = re.findall(r"[BDFH][1357]", my_input)
            i = re.findall(r"[ACEG][1357]", my_input)
            j = re.findall(r"[ACEG][2468]", my_input)
            if x: print("belongs to black square")
            elif y: print("belongs to white square")
            elif i: print("belongs to black square")
            elif j: print("belongs to white square")
        else: print("enter valid position")
else: print("enter valid position")
