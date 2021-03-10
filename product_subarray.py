def maxproduct(list_):
    ma = mi = total_ma = 1
    for i in range(0,len(list_)):

        if list_[i] >0:
            ma = list_[i]*ma
            mi = min(list_[i]*mi,mi)
        elif list_[i] == 0:
            ma = mi = 1
            pass
        else:
            temp_ma =ma
            ma = max(mi*list_[i],ma)
            mi = ma*list_[i]
        if total_ma < ma:
            total_ma =ma
    if total_ma == 1:
        return None
    return total_ma
        

# ar = [-2, 3, 4, -1, -2, 1, 5] 
# ar = [-2, -3, 0, 4, -1, -2, 1,0,  5, -3] 
# print(maxproduct(ar))