import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    edges = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        edges[a].append(b)
    
    # Sort each primary's secondary list
    for i in range(1, q + 1):
        edges[i].sort()
    
    match_primary = [0] * (q + 1)  # match_primary[a] = b
    match_secondary = [0] * (2 * q + 1)  # match_secondary[b] = a
    
    # Greedy: process secondaries in increasing order
    # We'll use a min-heap of available primaries for each secondary
    import heapq
    available = []
    sec_idx = q + 1
    # We'll iterate secondaries from q+1 to 2q
    for b in range(q + 1, 2 * q + 1):
        # Add all primaries that can connect to b
        # But we need to add primaries whose smallest edge <= b
        # Since edges are sorted, we can add incrementally
        pass
    
    # Better approach: sort all edges by b, then greedily assign
    all_edges = []
    for a in range(1, q + 1):
        for b in edges[a]:
            all_edges.append((b, a))
    all_edges.sort()
    
    used_primary = [False] * (q + 1)
    used_secondary = [False] * (2 * q + 1)
    result = []
    
    # Greedy: for each secondary in increasing order, assign smallest available primary
    # But we need to ensure we can cover all primaries eventually.
    # Since b - a >= 1, we can use a priority queue of primaries that become available.
    
    # We'll process secondaries from q+1 to 2q
    import heapq
    heap = []
    ptr = 0
    # all_edges sorted by b, then a
    for b in range(q + 1, 2 * q + 1):
        # push all primaries that can connect to b
        while ptr < len(all_edges) and all_edges[ptr][0] == b:
            a = all_edges[ptr][1]
            heapq.heappush(heap, a)
            ptr += 1
        # assign smallest available primary
        if heap:
            a = heapq.heappop(heap)
            if not used_primary[a] and not used_secondary[b]:
                used_primary[a] = True
                used_secondary[b] = True
                result.append((a, b))
    
    if len(result) == q:
        print("YES")
        for a, b in sorted(result):
            print(a, b)
    else:
        print("NO")

if __name__ == "__main__":
    solve()