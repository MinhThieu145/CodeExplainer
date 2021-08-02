def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    # loop vô tận đến khi dừng
    while True:
        # mức năng lượng khi nhảy vào mây (nếu như thundercloud thì c[i] = 1)
        energy = (energy - 1) - 2 * c[i]
        # công thức này để tính số của cloud tiếp theo (dấu % là để circular, tức là nó sẽ quay về 0)
        i = (i + k) % len(c)
        if i == 0:
            break
    return energy