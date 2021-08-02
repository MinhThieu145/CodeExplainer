def dayOfProgrammer(year):
    # trước năm 1918 tức là trước năm chuyển đổi
    if year<1918 :
        if year%4==0:
            # là năm nhuận, nên sẽ là 12 tháng 9 (đoạn này được đề cung cấp)
            return("12.09."+str(year))
        else:
            #năm không nhuận
            return("13.09."+str(year))
            
    elif year>1918:
        # năm nhuận sau 1918
        if year%400==0 or (year%4==0 and year%100!=0):
            return("12.09."+str(year))
        else:
        # năm không nhuận
            return("13.09."+str(year))   
    else:
        # trường hợp đặc biệt, là năm transition
        return("26.09.1918")