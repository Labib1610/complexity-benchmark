import sys
from itertools import permutations

def solve():
    data = sys.stdin.read().strip().split()
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    proposals = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        stages = []
        for _ in range(o):
            expert = int(data[idx]); idx += 1
            duration = int(data[idx]); idx += 1
            stages.append((expert, duration))
        proposals.append(stages)
    
    # State: for each proposal, which stage is next (index)
    # We'll do DFS over possible assignments.
    # We'll keep track of:
    # - next_stage_idx for each proposal
    # - available_time for each expert
    # - current_time (max of all finish times so far)
    
    n = j
    best = [float('inf')]
    
    def dfs(next_idx, expert_free, current_time):
        # next_idx: list of next stage index for each proposal
        # expert_free: list of time when each expert becomes free
        # current_time: current makespan so far
        
        # If all proposals done
        if all(idx >= len(proposals[i]) for i, idx in enumerate(next_idx)):
            best[0] = min(best[0], current_time)
            return
        
        # Prune: if current_time already >= best, stop
        if current_time >= best[0]:
            return
        
        # Find all possible assignments: for each proposal that has a next stage
        # and its expert is free at current_time, we can start it.
        # But we must consider that we can also wait for an expert.
        # We'll try all combinations of starting available jobs at current_time.
        
        # Collect possible actions
        possible_actions = []
        for i in range(n):
            if next_idx[i] < len(proposals[i]):
                expert, dur = proposals[i][next_idx[i]]
                start_time = max(current_time, expert_free[expert-1])
                possible_actions.append((i, expert, dur, start_time))
        
        # If no action possible, advance time to the next free expert
        if not possible_actions:
            next_time = min(expert_free)
            dfs(next_idx, expert_free, next_time)
            return
        
        # Try each possible action (or combination) - but to keep it simple,
        # we try starting one job at a time, and also try starting multiple simultaneously.
        # Since experts are independent, we can start all jobs whose experts are free at current_time.
        
        # We'll generate all subsets of possible actions that can start at current_time
        # (i.e., start_time == current_time)
        ready = [a for a in possible_actions if a[3] == current_time]
        
        # If none ready, advance time
        if not ready:
            next_time = min(a[3] for a in possible_actions)
            dfs(next_idx, expert_free, next_time)
            return
        
        # Try all subsets of ready actions (non-empty)
        from itertools import combinations
        for r in range(1, len(ready)+1):
            for combo in combinations(ready, r):
                # Check no expert conflict in combo
                experts_used = set()
                conflict = False
                for _, exp, _, _ in combo:
                    if exp in experts_used:
                        conflict = True
                        break
                    experts_used.add(exp)
                if conflict:
                    continue
                
                # Apply actions
                new_next = next_idx[:]
                new_free = expert_free[:]
                new_time = current_time
                for i, exp, dur, st in combo:
                    new_next[i] += 1
                    new_free[exp-1] = st + dur
                    new_time = max(new_time, st + dur)
                
                dfs(new_next, new_free, new_time)
        
        # Also try doing nothing and waiting for next event
        next_time = min(a[3] for a in possible_actions)
        if next_time > current_time:
            dfs(next_idx, expert_free, next_time)
    
    initial_next = [0]*n
    initial_free = [0]*m
    dfs(initial_next, initial_free, 0)
    
    print(best[0])

if __name__ == "__main__":
    solve()