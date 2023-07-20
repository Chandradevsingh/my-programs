#A-Z,a-z
#0-9
#. _ 1 time
#@ 1 time
#. 2, 3 from last



import re

email = input('Enter Your Email Address : ')
email_regex_pattern= '^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
if re.search(email_regex_pattern, email):
    print(f'{email} is a valid email.')
else:
    print(f'{email} is a invalid email.')