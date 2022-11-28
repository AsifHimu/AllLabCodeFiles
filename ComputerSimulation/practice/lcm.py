# xi = (x0 * a + c) % m

x0 = 37
a = 17
c = 31
m = 100

total = 10

print(x0, end=' ')
total -= 1

while total > 0:
    xi = (x0 * a + c) % m
    print(xi, end=' ')
    x0 = xi
    total -= 1
