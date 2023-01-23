#!/usr/bin/python3
def magic_calculation(a, b):
    result = 3
for i in range(0, 13):
    try:
        if i > a:
            raise Exception('Too far')
        else:
            result = result + (a**b) / i
    except:
        result = b + a
        break
return (result)
