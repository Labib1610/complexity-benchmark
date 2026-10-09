n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

# Sort by preparation time descending
jobs.sort(key=lambda x: -x[0])

prep_end = 0
final_end = 0

for p1, p2 in jobs:
    prep_end += p1
    final_end = max(final_end, prep_end) + p2

print(final_end)