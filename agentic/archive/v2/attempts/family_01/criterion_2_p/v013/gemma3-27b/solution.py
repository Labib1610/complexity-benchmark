def solve():
    n, m = map(int, input().split())
    incompatibilities = []
    for _ in range(m):
        u, v = map(int, input().split())
        incompatibilities.append((u, v))

    def is_valid(schedule):
        for u, v in incompatibilities:
            if schedule[u - 1] == schedule[v - 1]:
                return False
        return True

    def find_lexicographically_smallest_schedule():
        for i in range(2**n):
            schedule = []
            for j in range(n):
                if (i >> j) & 1:
                    schedule.append(1)
                else:
                    schedule.append(2)
            
            if is_valid(schedule):
                return schedule
        return None

    schedule = find_lexicographically_smallest_schedule()

    if schedule is None:
        print("NO")
    else:
        print("YES")
        print(*schedule)

solve()