def bigSorting(unsorted):
    # sử dụng lambda (do lambda khá là dài và phức tạp, nên trong TH này, lambda sử dụng len của từng elemen trong array để sort)
    # nếu như đều có cùng len thì covert qua int rồi sort
    unsorted.sort(key = lambda x:(len(x),int(x)))
    return unsorted