def solve():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    def is_valid(assignment):
        for u in range(1, n + 1):
            for v in adj[u]:
                if assignment[u-1] == assignment[v-1]:
                    return False
        return True

    def find_assignment(index, assignment):
        if index == n:
            if is_valid(assignment):
                return assignment
            else:
                return None

        for channel in [1, 2, 3]:
            new_assignment = assignment[:]
            new_assignment[index] = channel
            result = find_assignment(index + 1, new_assignment)
            if result:
                return result

        return None
    
    assignment = [0] * n
    result = find_assignment(0, assignment)

    if result:
        print("YES")
        print(*result)
    else:
        print("NO")

solve()