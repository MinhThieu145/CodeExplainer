def jumpingOnClouds(c):
    #lấy vị trí cloud
    last_cloud = len(c) - 1
    second_last_cloud = len(c) - 2

    vi_tri = 0
    step_count = 0
    # nếu như chưa phải là vị trí cuối hay gần cuối
    while vi_tri < second_last_cloud:
        # tránh thundercloud
        if c[vi_tri + 2]  == 0:
            vi_tri += 2
            
        else:
            vi_tri += 1
        step_count += 1
    # check xem nếu đang ở second_last_cloud thì +1.
    if vi_tri !=  last_cloud:
        step_count += 1
    
    return step_count