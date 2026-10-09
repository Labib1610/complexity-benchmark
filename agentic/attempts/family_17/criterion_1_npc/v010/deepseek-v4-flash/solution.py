import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    configs = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        configs.append((a - 1, b - 1, c - 1))
    
    # For each element, list of config indices that contain it
    elem_to_configs = [[] for _ in range(n)]
    for idx, (a, b, c) in enumerate(configs):
        elem_to_configs[a].append(idx)
        elem_to_configs[b].append(idx)
        elem_to_configs[c].append(idx)
    
    # Bitmask for each config
    config_masks = []
    for a, b, c in configs:
        config_masks.append((1 << a) | (1 << b) | (1 << c))
    
    used = [False] * t
    chosen = []
    full_mask = (1 << n) - 1
    
    # Backtracking with heuristic: pick uncovered element with fewest options
    def backtrack(covered_mask):
        if covered_mask == full_mask:
            return True
        # Find uncovered element with fewest available configs
        best_elem = -1
        best_options = []
        for elem in range(n):
            if not (covered_mask >> elem) & 1:
                options = [ci for ci in elem_to_configs[elem] if not used[ci] and (config_masks[ci] & covered_mask) == 0]
                if best_elem == -1 or len(options) < len(best_options):
                    best_elem = elem
                    best_options = options
                    if len(options) == 0:
                        return False
                    if len(options) == 1:
                        break
        for ci in best_options:
            used[ci] = True
            chosen.append(ci)
            if backtrack(covered_mask | config_masks[ci]):
                return True
            chosen.pop()
            used[ci] = False
        return False
    
    if backtrack(0):
        print("YES")
        for ci in chosen:
            a, b, c = configs[ci]
            print(a + 1, b + 1, c + 1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()