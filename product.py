def product(*args):
    if len(args) == 0:
        raise TypeError('参数输入错误')
    elif len(args) == 1:
        return args[0]
    else:
        mul = 1
        for n in args:
            mul = mul *n
        return mul

# print(product())

# print(product(5))

# print(product(5,6))

# print(product(5,6,7,9))

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('a测试失败!')
elif product(5, 6) != 30:
    print('b测试失败!')
elif product(5, 6, 7) != 210:
    print('c测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('d测试失败!')
else:
    try:
        product()
        print('e测试失败!')
    except TypeError:
        print('f测试成功!')