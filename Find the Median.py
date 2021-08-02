def findMedian(arr):
    # sort vì tìm median phải sort
    arr.sort()
    n  =len (arr)
    # nếu tổng số element là số lẻ, thì lấy số ở giữa
    if n % 2 == 1:
        return arr[n//2]
        
    else:
        # nếu là số chẵn, thì lấy 2 số ở giữa chia đôi. VD: (1,2,4,5) thì lấy 2 và 4 chia đôi
        return (arr[n//2 +1] + arr[n//2 - 1]) / 2