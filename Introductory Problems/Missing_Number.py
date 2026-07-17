n = int(input())
numbers = map(int,input().split())



expected_sum = int((n *(n+1))/2)
actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print(missing_number)