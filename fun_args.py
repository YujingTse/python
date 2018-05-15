def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    
f1(1,2)
    
f1(1,2,c=3)
    
f1(1,2,3,'a','b')
    
f1(1,2,3,'a','b',x=99)
    
f2(1,2,d=99,ext=None)

args_1 = (1,2,3,4)
args_2 = (1,2,3)
kw_1 = {'d':99,'x':'~'}
kw_2 = {'d':88,'x':'~'}

f1(*args_1,**kw_1)

f2(*args_2,**kw_2)