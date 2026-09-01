import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    comp_id = [-1] * n
    comps = []
    
    # Find connected components
    for i in range(n):
        if comp_id[i] == -1:
            cid = len(comps)
            stack = [i]
            comp_id[i] = cid
            nodes = []
            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in adj[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = cid
                        stack.append(v)
            comps.append(nodes)
    
    # Assign colors to components
    used_color = [False] * len(comps)
    for cid, nodes in enumerate(comps):
        # Try colors 1,2,3 in order
        for c in range(1, 4):
            if not used_color[c-1]:
                # Assign this color to all nodes in component
                for u in nodes:
                    color[u] = c
                used_color[c-1] = True
                break
    
    # Since each component is monochromatic, any assignment works
    # But we need lexicographically smallest: assign smallest possible color to each component in order of first occurrence
    # We already did that by iterating components in order of first vertex index.
    
    print("YES")
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    solve()