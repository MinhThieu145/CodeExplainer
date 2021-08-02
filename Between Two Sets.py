import math
# bài này thực ra gồm 3 bước nhé:
# tìm bội số nhỏ nhất của a
# tìm ước số lớn nhất của b
# có bao nhiêu số giữa ước số và bộ số chia hết cho bội số thì đó là kết quả
def getTotalX(a, b):
    count = 0
    # tìm bội số nhỏ nhất
    def get_GCD(a,b):
        print(a,b)
        return math.gcd(a,b)
    # tìm ước số lớn nhất
    def  get_LCD(a,b):
        if a == 0 or b == 0:
            return 0
        else:
            GCD = get_GCD(a,b)
            # công thức này có thể tìm trên mạng nhé, mình cũng không hiểu vì sao đâu !!
            return ((a * b)) // GCD
    
    # tìm ước số của list a bằng cách tính ước số 2 cặp 1, số thứ 1 với số thừ 2, rồi lấy kết quả đó với số thứ 3,....
    LCD = a[0]
    for i in a:
        LCD = get_LCD(i,LCD)
        
    # tính bội số NN của cả list b
    GCD = b[0]
    for i in b:
        GCD = get_GCD(i,GCD)

    # giữa chúng có bao nhiêu số thì đó là kết quả nhé
    chia = 0
    while chia<GCD:
        chia += LCD
        if GCD % chia == 0:
            count += 1
    return count