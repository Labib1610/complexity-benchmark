from itertools import permutations

def vault_allocation():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = {}
    for i in range(m):
        u, v = int(data[2 + 2*i]), int(data[3 + 2*i])
        if u not in edges:
            edges[u] = []
        if v not in edges:
            edges[v] = []
        edges[u].append(v)
        edges[v].append(u)

    compounds = list(range(1, n+1))
    
    for p in permutations([1, 2, 3], 3):
        assignment = {}
        possible = True
        
        for c in compounds:
            if c not in edges:
                continue
            forbidden_vaults = {assignment[v] for v in edges[c] if v in assignment}
            available_vaults = set(p) - forbidden_vaults
            
            if not available_vaults:
                possible = False
                break
            else:
                assignment[c] = min(available_vaults)
        
        if possible:
            result = [0] * n
            for c, vault in assignment.items():
                result[c-1] = vault
            for i in range(n):
                if result[i] == 0:
                    result[i] = p[0]
                    
            print("YES")
            print(" ".join(map(str, result)))
            return
    
    print("NO")

vault_allocation()