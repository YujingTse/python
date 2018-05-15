def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    elif len(L) == 1:
        return (L[0],L[0])
    else:
        Min = findMinAndMax(L[:-1])[0]
        Max = findMinAndMax(L[:-1])[1]
        if Min > L[-1]:
            Min = L[-1]
        if Max < L[-1]:
            Max = L[-1]
        return (Min,Max) 

# 测试
if findMinAndMax([]) != (None, None):
    print('a测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('b测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('c测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('d测试失败!')
else:
    print('e测试成功!')