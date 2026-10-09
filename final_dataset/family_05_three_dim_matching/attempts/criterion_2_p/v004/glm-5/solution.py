import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # specialist -> list of time slots
    spec_slots = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        spec_slots[x].append(z)
    
    # For each specialist, sort time slots and try greedy assignment
    for x in range(1, k + 1):
        spec_slots[x].sort()
    
    # Greedy: assign each specialist the smallest available time slot
    used = [False] * (k + 1)
    result = []
    
    for x in range(1, k + 1):
        found = False
        for z in spec_slots[x]:
            if not used[z]:
                used[z] = True
                result.append((x, x, z))  # machine = x per problem statement
                found = True
                break
        if not found:
            print("NO")
            return
    
    print("YES")
    for x, y, z in result:
        print(f"{x} {y} {z}")

solve()