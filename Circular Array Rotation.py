def circularArrayRotation(a, k, queries):
    # lấy length của array a
    j= len(a)

    # đảo kí tự cuối lần lượt lên đầu
    for x in range(k):
        n=a[j-1]
        a.insert(0,n)
        a.pop(j)

    newList= []
    # check những index yêu cầu và thêm vào list
    for m in queries:
        newList.append(a[m])

    return newList