n = int(input().strip())
a = []
for i in range(n):
    line = input().strip()
    a.append(list(map(int, line.split())))


def distance(a, k1, k2):
    print("x1=%d|x2=%d" % (k1, k2))
    d = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 1:
                d += abs(i - k1) + abs(j - k2)
    return d


x, y, c = 0, 0, 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            x += i
            y += j
            c += 1

X = x//c
Y = y//c
if c == n**2:
    print(-1)
else:
    print(min(distance(a, X, Y), distance(a, X + 1, Y + 1)))
