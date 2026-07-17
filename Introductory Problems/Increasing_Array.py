n = int(input())
arr = list(map(int,input().split()))

moves = 0

for indx, num in enumerate(arr):
    if indx == 0:
        continue
    
    previous = arr[indx-1]
    if num < previous:
        moves += previous - num
        arr[indx] = previous

print(moves)