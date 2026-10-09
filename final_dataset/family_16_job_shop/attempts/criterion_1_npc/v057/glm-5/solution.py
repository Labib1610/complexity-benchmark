import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    sequences = []
    for _ in range(j):
        o = int(next(it))
        seq = []
        for _ in range(o):
            inst = int(next(it))
            dur = int(next(it))
            seq.append((inst, dur))
        sequences.append(seq)

    # State: (index of next step for each sequence, end time of each instrument)
    # We use Dijkstra-like search over states.
    from heapq import heappush, heappop

    # Represent state as tuple of next step indices for each sequence
    start_state = tuple(0 for _ in range(j))
    # instrument end times
    start_inst = tuple(0 for _ in range(m))

    # Priority queue: (current_time, state, instrument_end_times)
    # We need to track best known time for each (state, instrument_end_times) but that's too large.
    # Instead, we can use a different approach: since j,m <=10 and steps <=50, we can do DFS with memoization
    # on state and instrument availability times.

    # Let's use a memo dictionary: key = (state_tuple, inst_times_tuple) -> earliest completion time
    # But inst_times can be large. However, we can normalize by subtracting min time.
    
    # Actually, a cleaner approach: simulate with backtracking/DFS.
    # At each step, we choose which sequence advances next.
    # We maintain for each sequence the earliest time its next step can start (when previous step finished).
    # We maintain for each instrument the time it becomes free.
    # We try all possible orders of executing steps.

    # Let's define:
    # seq_ready[i] = earliest time sequence i can start its next step
    # inst_free[k] = time instrument k becomes free
    # state = tuple of next step indices

    # We'll do DFS with memoization on (state, tuple(inst_free)) but normalized.
    # Since durations are up to 1000 and steps up to 50, times can be up to 50000.
    # But number of distinct states might be manageable.

    # Let's implement iterative deepening / Dijkstra.

    # Actually, let's do a DFS that tries all possible next steps to schedule.
    # We'll use memoization with key = (state, tuple(inst_free)).

    memo = {}

    def dfs(state, seq_ready, inst_free):
        # Check if all sequences are done
        if all(state[i] == len(sequences[i]) for i in range(j)):
            return 0  # no more steps, completion time is max of inst_free, but we track separately
        
        key = (state, tuple(inst_free))
        if key in memo:
            return memo[key]

        # We need to find the minimum completion time from this state.
        # We try scheduling each possible next step.
        best = float('inf')
        for i in range(j):
            if state[i] < len(sequences[i]):
                inst, dur = sequences[i][state[i]]
                # This step can start at max(seq_ready[i], inst_free[inst-1])
                start = max(seq_ready[i], inst_free[inst-1])
                end = start + dur
                # New state
                new_state = list(state)
                new_state[i] += 1
                new_state = tuple(new_state)
                new_seq_ready = list(seq_ready)
                new_seq_ready[i] = end
                new_inst_free = list(inst_free)
                new_inst_free[inst-1] = end
                # Recurse
                sub = dfs(new_state, tuple(new_seq_ready), tuple(new_inst_free))
                # The completion time is max(end, sub) but sub is relative to its own start?
                # Actually, we need to think carefully.
                # Let's redefine: dfs returns the earliest time when all remaining steps finish,
                # given the current inst_free and seq_ready.
                # So the total completion time from this point is max(end, sub_result) but
                # sub_result already accounts for everything after.
                # Wait, if we schedule step i now, it finishes at 'end'. The remaining steps
                # finish at some time >= end (since they can't start before their dependencies).
                # So the completion time is sub_result (which is >= end).
                # But we want the minimum over all choices.
                best = min(best, sub)
        
        memo[key] = best
        return best

    # Hmm, the above logic is flawed. Let me reconsider.
    # dfs should return the earliest completion time of all remaining steps.
    # When we schedule a step, it finishes at 'end'. The remaining steps finish at 'sub'.
    # The overall completion is max(end, sub) but sub is computed from the new state
    # which already has inst_free updated to 'end' for that instrument and seq_ready updated.
    # So sub >= end always? Not necessarily, because other instruments might be free later.
    # Actually, sub is the completion time of all remaining steps, which must be >= end
    # because at least the instrument we just used is busy until 'end'.
    # So completion = sub.
    # But we need to be careful: the initial call should return the max over all instruments
    # at the end.

    # Let me redefine: dfs returns the earliest time when all steps are done.
    # Base case: all done -> return max(inst_free) (but actually if all steps done,
    # the completion time is the max of all instrument free times, which equals
    # the max of all seq_ready times).

    # Let me rewrite properly.

    memo.clear()

    def dfs2(state, seq_ready, inst_free):
        if all(state[i] == len(sequences[i]) for i in range(j)):
            return max(seq_ready) if seq_ready else 0
        
        key = (state, seq_ready, inst_free)
        if key in memo:
            return memo[key]

        best = float('inf')
        for i in range(j):
            if state[i] < len(sequences[i]):
                inst, dur = sequences[i][state[i]]
                start = max(seq_ready[i], inst_free[inst-1])
                end = start + dur
                new_state = list(state)
                new_state[i] += 1
                new_state = tuple(new_state)
                new_seq_ready = list(seq_ready)
                new_seq_ready[i] = end
                new_seq_ready = tuple(new_seq_ready)
                new_inst_free = list(inst_free)
                new_inst_free[inst-1] = end
                new_inst_free = tuple(new_inst_free)
                sub = dfs2(new_state, new_seq_ready, new_inst_free)
                best = min(best, sub)
        
        memo[key] = best
        return best

    start_seq_ready = tuple(0 for _ in range(j))
    result = dfs2(start_state, start_seq_ready, start_inst)
    print(result)

solve()