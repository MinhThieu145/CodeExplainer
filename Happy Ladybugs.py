def happyLadybugs(b):
    from collections import Counter
    # counter sẽ ra 1 dictionary gồm name và số lần lặp, 
    # VD collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']) = {'b': 3, 'a': 2, 'c': 1}

    bugs = Counter(b)
    # nếu như màu không phải là "_" và chỉ lặp 1 lần, nghĩa là ta chỉ có màu đó 1 và không thể có cặp
    for (color, lan_lap) in bugs.items():
        if color != '_' and lan_lap == 1:
            return "NO"
    # nếu có chỗ trống, nghĩa là luôn có cách 
    if bugs['_'] > 0:
        return "YES"
    
    else:
        pair = 0
        # nếu như không có chỗ trống, thì không thể dịch chuyển được, do đó thứ tự buộc phải đúng (theo cặp)
        for i in range(len(b)-1):
            if b[i] == b[i+1]:
                pair += 1
            elif  b[i] != b[i+1] and pair >0:
                pair= 0
            else:
                return "NO"
    return "YES"
        