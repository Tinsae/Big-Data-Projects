# 13
numbers = [num for num in input().split(",") if int(num, 2) % 5 == 0 ]
print("".join(numbers))