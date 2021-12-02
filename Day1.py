# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


ccfile = open("D:\Downloads\AdventCodeDay1Input.txt", "r")
a = 0
b = 0
c = -1

for aline in ccfile:
    a = aline.split()
    a = int(a[0])
    if a > b:
       c = c + 1
    b = a


print(c)
ccfile.close()
