import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    mandated = [False] * (n + 1)
    for _ in range(t):
        u = int(next(iterator))
        mandated[u] = True
    
    edges = []
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        edges.append((w, u, v))
    
    # Sort edges by weight in descending order
    edges.sort(reverse=True)
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    mandated_count = [0] * (n + 1)
    for i in range(n + 1):
        if mandated[i]:
            mandated_count[i] = 1
            
    def find(i):
        # Path compression
        root = i
        while parent[root] != root:
            root = parent[root]
        while parent[i] != root:
            parent[i], i = root, parent[i]
        return root
    
    total_cost = 0
    
    for w, u, v in edges:
        root_u = find(u)
        root_v = find(v)
        
        if root_u != root_v:
            # Check if we can keep this edge
            # We can keep it if merging the two components doesn't make
            # the mandated_count equal to t (which would mean all mandated vars are connected)
            if mandated_count[root_u] + mandated_count[root_v] < t:
                # Merge
                if size[root_u] < size[root_v]:
                    root_u, root_v = root_v, root_u
                parent[root_v] = root_u
                size[root_u] += size[root_v]
                mandated_count[root_u] += mandated_count[root_v]
            else:
                # We must discard this edge, add its cost
                total_cost += w
                
    print(total_cost)

if __name__ == '__main__':
    solve()