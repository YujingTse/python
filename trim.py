def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])

# 测试:
if trim('hello  ') != 'hello':
    print('a测试失败!')
elif trim('  hello') != 'hello':
    print('b测试失败!')
elif trim('  hello  ') != 'hello':
    print('c测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('d测试失败!')
elif trim('') != '':
    print('e测试失败!')
elif trim('    ') != '':
    print('f测试失败!')
else:
    print('g测试成功!')