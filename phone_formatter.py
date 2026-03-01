import re

#your code goes here

phone_number = input()

pattern = r'00'

formatted_PN = re.sub(pattern,'+',phone_number,count=1)

print(formatted_PN)
