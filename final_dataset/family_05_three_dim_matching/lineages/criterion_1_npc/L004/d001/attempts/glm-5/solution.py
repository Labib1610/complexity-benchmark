import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    configs = []
    for _ in range(t):
        p1 = int(next(it))
        p2 = int(next(it))
        p3 = int(next(it))
        configs.append((p1, p2, p3))
    
    # State: (used_p1, used_p2, used_p3) as bitmasks
    # dp[state] = config_index that led to this state (or -2 if reachable, -1 if not)
    # We'll use a dict to map state -> prev_state and config used
    
    start = (0, 0, 0)
    dp = {start: (-1, -1)}  # state -> (prev_state, config_index)
    queue = [start]
    
    for depth in range(k):
        next_queue = []
        for state in queue:
            u1, u2, u3 = state
            for idx, (p1, p2, p3) in enumerate(configs):
                if (u1 >> (p1 - 1)) & 1:
                    continue
                if (u2 >> (p2 - 1)) & 1:
                    continue
                if (u3 >> (p3 - 1)) & 1:
                    continue
                n1 = u1 | (1 << (p1 - 1))
                n2 = u2 | (1 << (p2 - 1))
                n3 = u3 | (1 << (p3 - 1))
                new_state = (n1, n2, n3)
                if new_state not in dp:
                    dp[new_state] = (state, idx)
                    next_queue.append(new_state)
        queue = next_queue
        if not queue:
            print("NO")
            return
    
    # Find a state with exactly k bits set in each mask
    target_mask = (1 << k) - 1
    final_state = None
    for state in queue:
        if state[0] == target_mask and state[1] == target_mask and state[2] == target_mask:
            final_state = state
            break
    
    if final_state is None:
        print("NO")
        return
    
    # Reconstruct path
    result = []
    state = final_state
    while state != start:
        prev_state, idx = dp[state]
        result.append(configs[idx])
        state = prev_state
    
    print("YES")
    for config in result:
        print(f"{config[0]} {config[1]} {config[2]}")

if __name__ == "__main__":
    solve()