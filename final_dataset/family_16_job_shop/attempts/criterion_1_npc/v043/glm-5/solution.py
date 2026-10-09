import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    dossiers = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        steps = []
        for _ in range(o):
            c = int(data[idx]); idx += 1
            d = int(data[idx]); idx += 1
            steps.append((c, d))
        dossiers.append(steps)
    
    # State: (time, clerk_free_times, dossier_progress)
    # clerk_free_times: tuple of m ints
    # dossier_progress: tuple of j ints (index of next step for each dossier)
    
    initial_clerk = tuple([0] * m)
    initial_progress = tuple([0] * j)
    
    # Use Dijkstra-like approach
    # State: (time, clerk_free, progress)
    # We want to minimize the max time when all dossiers are done
    
    visited = {}
    heap = [(0, initial_clerk, initial_progress)]
    
    while heap:
        time, clerk_free, progress = heappop(heap)
        
        key = (clerk_free, progress)
        if key in visited:
            continue
        visited[key] = time
        
        # Check if all dossiers are done
        all_done = True
        for i in range(j):
            if progress[i] < len(dossiers[i]):
                all_done = False
                break
        
        if all_done:
            print(time)
            return
        
        # Find the next possible action
        # We can advance any dossier that is ready (its next clerk is free)
        # But we need to be careful: we should advance in a way that doesn't block
        
        # Actually, the key insight: we should advance the dossier whose next clerk
        # becomes free earliest, or we can wait
        
        # Let's think differently: at any point, we can choose to start a step
        # for any dossier whose next clerk is free at the current time or later
        
        # The state space is small enough for Dijkstra
        
        for i in range(j):
            if progress[i] < len(dossiers[i]):
                clerk, dur = dossiers[i][progress[i]]
                clerk_idx = clerk - 1
                
                # This dossier can start when:
                # 1. The clerk is free (clerk_free[clerk_idx])
                # 2. The previous step of this dossier is done
                #    Since we track progress, the previous step is done when we advance progress
                #    But we need to track when each dossier finished its last step
                
                # Hmm, we're not tracking when each dossier finished its previous step
                # We need to add that to the state
        
        # Redesign: state includes when each dossier is ready for next step
        pass
    
    # Let me redesign the state
    # State: (clerk_free_times, dossier_ready_times, progress)
    # But this might be too large
    
    # Alternative: since total steps <= 50, and j,m <= 10
    # We can simulate with a priority queue where we pick which step to execute next
    
    # Actually, let's think about it as: at each decision point, we choose which
    # available (dossier, clerk) pair to execute. The start time is max(clerk_free, dossier_ready)
    
    # State: (clerk_free_times, dossier_ready_times, progress_indices)
    # clerk_free: m values, dossier_ready: j values, progress: j values
    # Each value 0..~50000, but we can use Dijkstra
    
    # Let's bound: total steps = 50, each step up to 1000, so max time = 50000
    # State space could be large but with Dijkstra and pruning it should work
    
    # Actually, let's think more carefully. The state is determined by:
    # - For each clerk: when they become free
    # - For each dossier: which step they're on and when they're ready
    
    # But the "when they're ready" for a dossier is determined by when its previous step finished
    # which is one of the clerk free times (after the step). So it's redundant?
    
    # No, because a dossier's ready time = end time of its last completed step
    # which is a clerk_free time that was set when we advanced that dossier
    
    # So we need to track it separately
    
    # Let me just implement with the full state
    
    initial_state = (tuple([0]*m), tuple([0]*j), tuple([0]*j))
    visited2 = {}
    heap2 = [(0, initial_state)]
    
    while heap2:
        max_time, (clerk_free, dossier_ready, progress) = heappop(heap2)
        
        key = (clerk_free, dossier_ready, progress)
        if key in visited2:
            continue
        visited2[key] = max_time
        
        all_done = True
        for i in range(j):
            if progress[i] < len(dossiers[i]):
                all_done = False
                break
        
        if all_done:
            print(max_time)
            return
        
        for i in range(j):
            if progress[i] < len(dossiers[i]):
                clerk, dur = dossiers[i][progress[i]]
                clerk_idx = clerk - 1
                
                start = max(clerk_free[clerk_idx], dossier_ready[i])
                end = start + dur
                
                new_clerk = list(clerk_free)
                new_clerk[clerk_idx] = end
                new_clerk = tuple(new_clerk)
                
                new_ready = list(dossier_ready)
                new_ready[i] = end
                new_ready = tuple(new_ready)
                
                new_progress = list(progress)
                new_progress[i] += 1
                new_progress = tuple(new_progress)
                
                new_max = max(max_time, end)
                
                new_key = (new_clerk, new_ready, new_progress)
                if new_key not in visited2 or visited2[new_key] > new_max:
                    heappush(heap2, (new_max, new_key))
    
    print(0)

solve()