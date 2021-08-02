def insertionSort1(n, arr):
    # đặt target
    key = arr[-1]
    # đặt index
    i = n -1 
    # loop qua array từ phải qua trái
    # nếu như bên trái của i nhỏ hơn i (vị trí để insert key vào) thì dừng lại
    while i > 0 and arr [i - 1] > key:
        arr[i] = arr[i -1]
        # dùng map để convert int trong list qua string (do join không dùng với int)
        print(' '.join(map(str,arr)))
        i -= 1
    arr[i] = key
    print(' '.join(map(str,arr)))