"""
The below code takes a string as input and return True if the string is a valid IPV4 address.

Input:

0.0.0.0

Output:

True

Input:

198.25.12.3

Output:

True
"""

def validateIP(ip):
    if not ip:
        return False
    if len(ip) >15:
        return False
    cnt_dots =0
    for a in ip:
        if a == '.':
            cnt_dots += 1
    if cnt_dots != 3:
        return False
    if ip[0] == '.'  or ip[len(ip)-1] == '.':
        return False
    
    l = ip.split('.')
    if len(l)!=4:
        return False
    for i,a in enumerate(l):
        if a.isdigit() != True:
            return False
        if len(a) >3:
            return False
        if len(a) >1 and a[0] == '0':
            return False
        if int(a) < 0 or int(a) > 255:
            return False
    return True 


