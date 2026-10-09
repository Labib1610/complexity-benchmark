n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Sort by assembly time descending
jobs.sort(key=lambda x: x[1], reverse=True)

prep_end = 0
assembly_end = 0

for p1, p2 in jobs:
    prep_end += p1
    assembly_end = max(assembly_end, prep_end) + p2

print(assembly_end)