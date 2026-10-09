```python
def solve():
    nA, nB, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    
    adjA = [[] for _ in range(nA + 1)]
    adjB = [[] for _ in range(nB + 1)]
    
    for a, b in edges:
        adjA[a].append(b)
        adjB[b].append(a)