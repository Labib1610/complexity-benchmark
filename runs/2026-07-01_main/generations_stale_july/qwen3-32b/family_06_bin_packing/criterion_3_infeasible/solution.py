n, C = map(int, input().split())
w = list(map(int, input().split()))
for i in range(n):
    if w[i] > C:
        print(i + 1)
        break