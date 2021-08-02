def appendAndDelete(s, t, k):
    # đếm kí tự lặp
    the_same_count = 0
    # dùng function zip để do theo cặp trong string s và t
    for (i,j) in zip(s,t):
        if i == j:
            # nếu giống thì counter +1
            the_same_count += 1
        else:
            # không giống nghĩa là phải dừng lại và xóa từ đó
            break
    # Tính kí tự phải xóa
    delete_cha = len(s) - the_same_count
    # tính kí tự add thêm
    add_cha = len(t) - the_same_count
    
    if (delete_cha + add_cha) == k or k > (len(s) + len(t)):
        return "Yes"
    elif (delete_cha + add_cha) < k:
        total_de_ad = delete_cha + add_cha
        while total_de_ad < k:
            total_de_ad += 2
            if total_de_ad == k:
                
                return "Yes"
            elif total_de_ad >k and delete_cha < len(s):
                return "No"
            
               
        return "Yes"
    
    else:
        return "No"