txtfile = open("D:\Downloads\AdventCodeDay2Input.txt", "r")

horizontalPos = 0
depth = 0
aim = 0

for aline in txtfile:
    command = aline.split()

    if command[0] == "forward":
       horizontalPos = horizontalPos + int(command[1])
       depth = depth + (aim * int(command[1]))
    elif command[0] == "down":
        aim = aim + int(command[1])
    elif command[0] == "up":
        aim = aim - int(command[1])

print(horizontalPos * depth)

txtfile.close()
