import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    n = 3 * q
    
    logs = []
    person_to_logs = [[] for _ in range(n + 1)]
    
    for i in range(t):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        c = int(input_data[idx]); idx += 1
        logs.append((a, b, c))
        person_to_logs[a].append(i)
        person_to_logs[b].append(i)
        person_to_logs[c].append(i)
    
    if q == 0:
        print("YES")
        return
    
    # Find the person in the fewest logs - start there for better pruning
    # But simpler: always cover smallest uncovered person
    
    used = [False] * (n + 1)
    chosen = []
    
    def backtrack():
        if len(chosen) == q:
            return True
        
        # Find smallest uncovered person
        target = -1
        for p in range(1, n + 1):
            if not used[p]:
                target = p
                break
        
        # Try all logs containing target that don't conflict
        for log_idx in person_to_logs[target]:
            a, b, c = logs[log_idx]
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                chosen.append(log_idx)
                if backtrack():
                    return True
                chosen.pop()
                used[a] = used[b] = used[c] = False
        
        return False
    
    if backtrack():
        print("YES")
        for log_idx in chosen:
            a, b, c = logs[log_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

solve()