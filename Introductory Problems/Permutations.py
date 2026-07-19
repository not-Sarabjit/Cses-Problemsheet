n = int(input())


# There are 2 ways to do this, First is creating an ascending order list from 1 to n and then picking one element from left and then one element from right and moving closer from both sides after each iteration
# and then at the end, swapping the first and last elements from the resultant list. But for  n = 4, we will have to swap the first and second last element instead of first and last

# Second is, if we first print all even and then all odd numbers from 1 to n



if n == 1:
    print(1)
elif n <= 3:
    print('NO SOLUTION')
else:
    for i in range(2,n+1,2):
        print(i,end= ' ')
    for i in range(1,n +1,2):
        print(i, end = ' ')

