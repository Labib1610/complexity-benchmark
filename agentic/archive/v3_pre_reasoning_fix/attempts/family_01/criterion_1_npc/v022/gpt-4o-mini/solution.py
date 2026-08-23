def is_valid_assignment(n, adj, assignment):
    for u in range(n):
        for v in adj[u]:
            if assignment[u] == assignment[v]:
                return False
    return True

def backtrack(n, adj, assignment, index):
    if index == n:
        if is_valid_assignment(n, adj, assignment):
            return assignment[:]
        return None
    
    for bus in range(1, 4):
        assignment[index] = bus
        result = backtrack(n, adj, assignment, index + 1)
        if result is not None:
            return result
    return None

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    adj = [[] for _ in range(n)]
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    
    assignment = [0] * n
    result = backtrack(n, adj, assignment, 0)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()