power = int(input("Enter a number: "))
starter = power
for expo in range(16):
    print(f"{starter} to the power of", expo, "is", power)
    power *= starter
