def count_multiples(nums):
    divisor_count = {i: 0 for i in range(1, 10)}
    for num in nums:
        for i in range(1, 10):
            if num % i == 0:
                divisor_count[i]+=1
    return divisor_count
input_string=input("Enter numbers separated by commas (eg. 1,2,5,6,7): ")
nums=list(map(int, input_string.split(',')))
result=count_multiples(nums)
print(result)