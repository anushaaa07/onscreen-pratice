# import re
# txt=input("Please enter credit card number: ") 
# pattern="^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$"
# test=re.findall(pattern,txt) 
# if len(test):
#  print("Credit card number is valid") 
# else:
#  print("Credit card number is not valid")
import re
Txt ="""Dave Martin 
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com

Charles Harris 
800-555-5669
969 High St., Atlantis VA 34075
charlesharris@bogusemail.com

Eric Williams 
560-555-5153
806 1st St., Faketown AK 86847 
laurawilliams@bogusemail.com

Corey Jefferson 
900-555-9340
826 Elm St., Epicburg NE 10671
coreyjefferson@bogusemail.com"""

phone_numbers='\d{3}[-]\d{3}[-]\d{4}' 
phone_numbers=re.findall(phone_numbers,Txt) 
print(phone_numbers)
