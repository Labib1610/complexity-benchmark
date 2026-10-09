import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])
    
    idx = 3
    T = set()
    for _ in range(t):
        T.add(int(input_data[idx]))
        idx += 1
        
    edges = []
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        w = int(input_data[idx+2])
        idx += 3
        edges.append((w, u, v))
        
    if t <= 1:
        print(0)
        return
        
    edges.sort()
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    comp_size = [1] * (n + 1)
    t_count = [1 if i in T else 0 for i in range(n + 1)]
    
    total_cost = 0
    
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
        
    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if rank[ru] < rank[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            comp_size[ru] += comp_size[rv]
            t_count[ru] += t_count[rv]
            if rank[ru] == rank[rv]:
                rank[ru] += 1
            if t_count[ru] == t:
                total_cost += w * (comp_size[ru] - 1)
                t_count[ru] = 0
                
    print(total_cost)

if __name__ == '__main__':
    solve()