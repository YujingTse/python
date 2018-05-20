# -*- coding: utf-8 -*-

def is_palindrome(n):
        
    a = 0 
    k = n
    while k: 
        a = a * 10 + k % 10
        k = k // 10
    return a == n

# 测试:
output = filter(is_palindrome, range(1,1000))
print('1~1000:', list(output))