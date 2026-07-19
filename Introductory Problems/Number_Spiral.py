for _ in range(int(input())):
    x,y = map(int,input().split())
    bigger_cord = max(x,y)
    max_val_in_row = bigger_cord **2
    if  bigger_cord %2 == 1:
        fin_x,fin_y = 1,bigger_cord
    else:
        fin_x,fin_y = bigger_cord,1
    final_answer = max_val_in_row - abs(fin_x - x)
    final_answer = final_answer - abs(fin_y- y)
    print(final_answer)