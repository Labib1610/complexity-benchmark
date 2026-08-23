def is_valid(vaults, u, v):
    return vaults[u] != vaults[v]

def assign_vaults(n, m, incompatible):
    from itertools import product

    for vaults in product(range(1, 4), repeat=n):
        if all(is_valid(vaults, u - 1, v - 1) for u, v in incompatible):
            return vaults
    return None

import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatible = [tuple(map(int, line.split())) for line in data[1:m+1]]

vault_assignment = assign_vaults(n, m, incompatible)

if vault_assignment:
    print("YES")
    print(" ".join(map(str, vault_assignment)))
else:
    print("NO")