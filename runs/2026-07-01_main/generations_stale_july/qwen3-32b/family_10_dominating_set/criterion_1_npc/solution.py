import itertools

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    k = int(input[idx]); idx +=1

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(input[idx]); idx +=1
        v = int(input[idx]); idx +=1
        adj[u].append(v)
        adj[v].append(u)

    if k == 0:
        print("NO")
        return

    coverage_masks = [0] * (n + 1)
    full_mask = (1 << n) - 1

    for u in range(1, n + 1):
        mask = 0
        mask |= 1 << (u - 1)
        for v in adj[u]:
            mask |= 1 << (v - 1)
        coverage_masks[u] = mask

    # Sort nodes by coverage size descending to prioritize better candidates
    nodes = list(range(1, n + 1))
    nodes.sort(key=lambda x: bin(coverage_masks[x]).count('1'), reverse=True)

    found = False
    max_t = min(k, n)
    for t in range(1, max_t + 1):
        for combo in itertools.combinations(nodes, t):
            combo_mask = 0
            for node in combo:
                combo_mask |= coverage_masks[node]
                if combo_mask == full_mask:
                    break  # Early exit if full coverage is achieved
            if combo_mask == full_mask:
                print("YES")
                print(' '.join(map(str, combo)))
                found = True
                break
        if found:
            break

    if not found:
        print("NO")

if __name__ == "__main__":
    main()