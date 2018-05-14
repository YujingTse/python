import math

def quadratic(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('这是恒等式')
                return None
            else:
                print('这是恒不等式')
                return None
        else:            
            print('这不是一元二次方程式，x = %.2f' % (-c/b))
            return -c/b
    elif b * b - 4 * a * c < 0:
        print('ax2+bx+c=0无解')
        return None
    elif b * b - 4 * a * c == 0:
        print('ax2+bx+c=0的解x = %.2f' % (-b/(2*a)))
        return -b/(2*a)
    else:
        m = b*b-4*a*c
        z = math.sqrt(m)
        print('ax2+bx+c=0的解x1 = %.2f,x2 = %.2f' % ((-b+z)/(2*a),(-b-z)/(2*a)))
        return (-b+z)/(2*a),(-b-z)/(2*a)

def main():
    a = int (input("Please input a:"))
    b = int (input("Please input b:"))
    c = int (input("Please input c:"))
    q = quadratic(a,b,c)
    print(q)
    if q: 
        print("无解") 
    elif len(q) == 1:
        if a == 0:
            if q == -c/b:
                print('测试成功')
            else:
                print('测试失败')
        else:
            if q == -b/(2*a):
                print("测试成功")
            else:
                print('测试失败')
    elif len(q) == 2:
        if q == ((-b+math.sqr(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)):
            print('测试正确')
        else:
            print('测试失败')
    else:
        print('测试失败')
    return
    
main()