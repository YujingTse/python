# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):

    n = s.index('.')
    s1 = s[0:n]
    s2 = s[n+1:]

    def char2num(s):
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[s]
    
    return reduce(lambda x,y:10*x+y,map(char2num,s1+s2))/10**n
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')