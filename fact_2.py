def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
    
print(fact(1))

print(fact(6))

print(fact(1000))