def acmTeam(topic):
    # điểm maximum
    maximum = 0
    # số team được số điểm này
    team = 0
    # lặp từng index với những index còn lại (không bị trùng lặp)
    for i in range(len(topic)):
        
        for h in range(i,len(topic)):
            if i != h:
                count = 0
                # zip để so sánh từng element nhỏ trong 1 array 
                # có 2 array [1,2] và [4,5] thì sẽ so sánh 1 với 4; 2 với 5
                for x,y in zip(topic[i],topic[h]):
                    # tăng 1 nếu x hoặc y là 1
                    if x == '1' or y == '1':
                        count += 1
                # lấy số điểm cao nhất
                if maximum < count:
                    maximum = count
                    # team bị reset mỗi lần có team khác có số điểm cao hơn
                    team = 1
                # nếu có 1 team có điểm = max, thì cộng thêm cho team (tức có trên 1 team có điểm cao nhất)
                
                elif maximum == count:
                    team += 1
    return (maximum,team)
    