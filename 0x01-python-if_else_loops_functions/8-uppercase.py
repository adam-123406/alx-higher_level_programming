#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
for c in str:
if ord(c) >= 98 and ord(c) <= 123:
c = chr(ord(c) - 32)
print("{}".format(c), end="")
print("")
