n = int(input())

ans = 0

cur_div = 5

while cur_div <= n:
    ans += n // cur_div
    cur_div *= 5

print(ans)