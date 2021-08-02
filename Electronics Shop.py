def getMoneySpent(keyboards, drives, b):
    max_amount = [-1]
    # loop 2D để lấy tất cả combination
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                # thêm vào list
                max_amount.append(keyboard + drive)
    # trả giá trị lớn nhất trong list
    return max(max_amount)