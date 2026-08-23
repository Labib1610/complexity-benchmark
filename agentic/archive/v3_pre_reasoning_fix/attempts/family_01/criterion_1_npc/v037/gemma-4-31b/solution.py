import sys

def solve():
    # Read n and m from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # assignment[i] stores the shift of worker i (1, 2, or 3)
    assignment = [0] * n

    def is_valid(worker, shift):
        for neighbor in adj[worker]:
            if assignment[neighbor] == shift:
                return False
        return True

    def backtrack(worker):
        if worker == n:
            return True
        
        # Try shifts 1, 2, 3 in increasing order to find the lexicographically smallest sequence
        for shift in (1, 2, 3):
            if is_valid(worker, shift):
                assignment[worker] = shift
                if backtrack(worker + 1):
                    return True
                assignment[worker] = 0
        
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for safety, though n is only 40
    sys.setrecursionlimit(2000)
    solve()