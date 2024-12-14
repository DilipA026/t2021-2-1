def generate_numbers(a):
    numbers = []
    for i in range(a):
        numbers.append(2 * i + 1)
    return ', '.join(map(str, numbers))
a = int(input("Enter a number: "))
print(generate_numbers(a))