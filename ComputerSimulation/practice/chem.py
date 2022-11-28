delta_t = 0.1
A0 = 100
B0 = 50
C0 = 0

k1 = 0.008
k2 = 0.002

t = 0
T = 5

print("\tTime\t\tA[i]\t\tB[i]\t\tC[i]")
print("%8.2f %11.2f %11.2f %11.2f" % (t, A0, B0, C0))
t += delta_t
while t < T:
    A = A0 + (k2 * C0 - k1 * A0 * B0) * delta_t
    B = B0 + (k2 * C0 - k1 * A0 * B0) * delta_t
    C = C0 + (2 * k1 * A0 * B0 - 2 * k2 * C0) * delta_t
    A0, B0, C0 = A, B, C
    print("%8.2f %11.2f %11.2f %11.2f" % (t, A0, B0, C0))
    t += delta_t
