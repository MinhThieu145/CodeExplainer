def flatlandSpaceStations(n, c):
    largest_dis = 0
    c.sort()
    print(c)
    # lấy length lớn nhất giữa các space station với nhau, VD có station 0,4,6 thì lấy khoảng cách giữa 0 và 4, 4 và 6, 
    for i in range(1,len(c)):
        largest_dis = max(largest_dis,(c[i] - c[i-1]) // 2)
    # so sánh khoảng cách lớn nhất trong số trên, với khoảng cách từ city đầu tiên (là 0) đến space station gần nhất, là c[0] do đã 
    # sắp xếp
    # và so sánh khoảng cách spacestation gần nhất của city cuối cùng (city c[-1] sau khi sắp xếp)
    largest_dis = max(largest_dis, c[0], (n-1) - c[-1])
    return largest_dis