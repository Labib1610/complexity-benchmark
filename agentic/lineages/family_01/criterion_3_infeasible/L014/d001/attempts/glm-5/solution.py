import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx + 1])
        idx += 2
        adj[u].add(v)
        adj[v].add(u)
    
    # Find lexicographically smallest triangle
    for a in range(1, n + 1):
        adj_a = adj[a]
        # Iterate over neighbors b > a
        for b in adj_a:
            if b > a:
                # For each neighbor c of b with c > b, check if c is adjacent to a
                for c in adj[b]:
                    if c > b and c in adj_a:
                        sys.stdout.write(f"{a} {b} {c}\n")
                        return

if __name__ == "__main__":
    solve()