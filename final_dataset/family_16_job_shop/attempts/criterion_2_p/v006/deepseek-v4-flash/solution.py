n = int(input())
containers = [tuple(map(int, input().split())) for _ in range(n)]

# Sort by loading time descending
containers.sort(key=lambda x: x[1], reverse=True)

inspection_end = 0
max_finish = 0

for p1, p2 in containers:
    inspection_end += p1
    max_finish = max(max_finish, inspection_end + p2)

print(max_finish)