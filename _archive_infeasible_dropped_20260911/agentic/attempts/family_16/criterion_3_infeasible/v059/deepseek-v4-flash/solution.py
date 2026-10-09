j, T = map(int, input().split())

sum1 = 0
sum2 = 0

for i in range(1, j + 1):
    p1, p2 = map(int, input().split())
    if p1 + p2 > T:
        print(f"JOB {i}")
        exit()
    sum1 += p1
    sum2 += p2

if sum1 > T:
    print("LOAD 1")
elif sum2 > T:
    print("LOAD 2")