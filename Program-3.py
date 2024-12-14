count = int(input("Enter count number: "))
if count % 2 != 1:
    count -= 1

for i in range(count):
    if i < count - 1:
        print(2 * i + 1, end=", ")
    else:
        print(2 * i + 1)