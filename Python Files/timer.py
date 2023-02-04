import time

count = int(input("Start timer for how many seconds: ")) + 1
starter = 0

for i in range(1, count):
    starter += 1
    print(f"{starter} Mississippi")
    time.sleep(1)

print("Done")
