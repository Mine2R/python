for N in range(2, 1001):
    premier = True
    for i in range (2, N):
        if N % i == 0:
            premier = False
            break
    if premier:
        print(N)
    