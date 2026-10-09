import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    nodes = []
    for _ in range(n):
        p1 = int(next(it))
        p2 = int(next(it))
        nodes.append((p1, p2))
    
    # Sort by key: p1 if p1 <= p2, else -p2
    # This is equivalent to sorting by (p1 <= p2, p1 if p1 <= p2 else -p2)
    # Nodes with p1 <= p2 come first, sorted by p1 ascending
    # Nodes with p1 > p2 come after, sorted by p2 descending
    nodes.sort(key=lambda x: (x[0] > x[1], x[0] if x[0] <= x[1] else -x[1]))
    
    C = 0
    E = 0
    for p1, p2 in nodes:
        C += p1
        if C > E:
            E = C
        E += p2
    
    print(E)

if __name__ == "__main__":
    solve()