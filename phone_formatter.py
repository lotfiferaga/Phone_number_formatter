import re

#your code goes here

phone_number = input()

pattern = r'00'

if re.match(pattern,phone_number) :
    formatted_PN = re.sub(pattern,'+',phone_number,count=1)
    print(formatted_PN)
else :
    formatted_PN = phone_number
    print(formatted_PN)
