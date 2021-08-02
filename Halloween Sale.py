def howManyGames(p, d, m, s):
    games = 0
    # trong khi còn đủ tiền (tiền nhiều hơn giá game)

    while p <= s:
        
        s -= p
        # giá game giảm đến khi chạm mốc m, thì sẽ giữ nguyên ở m
        p = max(p-d,m)
        games += 1

    return games
