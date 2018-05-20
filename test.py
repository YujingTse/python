def f(n):
     a = 0
     k = n
     print('A:',k)
     while k:
         a = a * 10 + k % 10
         k = k// 10
         print('B:',a,'C:',k)
     if a == n:
         return True
     else:
         return False
         
f(12321)