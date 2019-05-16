# 递归与尾递归

#递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))

# 尾递归

def fact2(n):
    return fact2(n, 1)

def fact2(num, result):
    if num == 1:
        return result
    return fact2(num - 1, result * num)

print(fact2(5, 1))

# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)

def main():
    move(3, 'A', 'B', 'C')

if __name__ == '__main__':
    main()

