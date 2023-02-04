#  making a 2d pyramid with blocks

blocks = int(input("Enter the number of blocks: "))
height = 0

while True:
    if blocks > 1:
        height += 1
        blocks -= height
    else:
        if height == 0 and blocks == 1:
            height = 1
        elif height <= 0 and blocks < 0:
            height = 0
        elif blocks < 0:
            height -= 1
        break

print("The height of the pyramid:", height)
