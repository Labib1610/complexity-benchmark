n = int(input())
pos = []
neg = []
for _ in range(n):
    p1, p2 = map(int, input().split())
    if p2 >= p1:
        pos.append((p1, p2))
    else:
        neg.append((p1, p2))

pos.sort(key=lambda x: x[0])
neg.sort(key=lambda x: -x[1])

charge = 0
cost = 0

for p1, p2 in pos + neg:
    if charge < p1:
        cost += p1 - charge
        charge = p1
    charge -= p1
    charge += p2
    cost += p2

print(cost)