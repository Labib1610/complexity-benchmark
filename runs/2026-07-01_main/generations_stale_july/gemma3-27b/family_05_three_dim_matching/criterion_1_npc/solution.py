def solve():
    k, t = map(int, input().split())
    combinations = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        combinations.append((x, y, z))

    def is_valid(crews):
        specialists = set()
        machines = set()
        time_slots = set()
        for x, y, z in crews:
            specialists.add(x)
            machines.add(y)
            time_slots.add(z)
        return len(specialists) == k and len(machines) == k and len(time_slots) == k

    import itertools
    for crews in itertools.combinations(combinations, k):
        if is_valid(crews):
            print("YES")
            for x, y, z in crews:
                print(x, y, z)
            return

    print("NO")

solve()