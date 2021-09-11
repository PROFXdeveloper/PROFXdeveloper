import re


num_of_phones = int(input())


for i in range (num_of_phones):
    phone_no = input().strip()
    
    if len (re.findall(r'^[7-9]\d{9}$', phone_no)) !=0:
        print("YES")
    else:
        print("NO")
