import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    docs = []
    for _ in range(j):
        o = int(next(it))
        seq = []
        for _ in range(o):
            off = int(next(it))
            dur = int(next(it))
            seq.append((off-1, dur))
        docs.append(seq)
    
    # State: (time, doc_positions, official_free_times)
    # doc_positions: tuple of next review index for each doc
    # official_free_times: tuple of when each official is free
    start_pos = tuple(0 for _ in range(j))
    start_off = tuple(0 for _ in range(m))
    start = (0, start_pos, start_off)
    visited = {(start_pos, start_off): 0}
    heap = [start]
    
    while heap:
        time, pos, off_free = heappop(heap)
        key = (pos, off_free)
        if visited.get(key, float('inf')) < time:
            continue
        
        # Check if all done
        all_done = True
        for i in range(j):
            if pos[i] < len(docs[i]):
                all_done = False
                break
        if all_done:
            print(time)
            return
        
        # Try scheduling each document's next review
        for i in range(j):
            if pos[i] < len(docs[i]):
                off, dur = docs[i][pos[i]]
                # This review can start at max(time, off_free[off])
                start_time = time if time > off_free[off] else off_free[off]
                end_time = start_time + dur
                new_pos = list(pos)
                new_pos[i] += 1
                new_pos = tuple(new_pos)
                new_off = list(off_free)
                new_off[off] = end_time
                new_off = tuple(new_off)
                new_key = (new_pos, new_off)
                new_time = end_time
                # The "time" for next state is the minimum of current time and end_time?
                # Actually we need to track when we can make next decision
                # The state time should be the max of all official free times that are relevant
                # But simpler: use end_time as the time, but we might miss parallel schedules
                # Let's use the minimum time at which we can make a decision
                # which is min of all official free times and current time
                # Actually the correct approach: time is the current decision point
                # After scheduling, the next decision point is the minimum of:
                # - other officials' free times
                # - the end time of this review
                # But we need to be careful
                
                # Let's compute the next decision time as min of all off_free times and end_time
                # But we already have time as the current decision point
                # After this scheduling, the next time we can make a decision is
                # the minimum of all official free times (including the updated one)
                # But we also need to consider that we might want to schedule at a time
                # before end_time if another official is free
                
                # The state should track: (next_decision_time, pos, off_free)
                # where next_decision_time = min(off_free) but at least time?
                # Actually, let's just push (end_time, new_pos, new_off) and also
                # we need to allow scheduling at times before end_time
                
                # Better approach: the time in the state is the earliest time we can make
                # a new decision. After scheduling doc i on official off ending at end_time,
                # the earliest next decision is min of all official free times.
                # But we also have the current time which might be earlier than some free times.
                
                # Let's compute next_time = min(new_off) but this might be less than time
                # Actually new_off[off] = end_time >= time, and other new_off[k] = off_free[k] >= time? No.
                # off_free[k] could be < time? No, because time is the current decision point
                # and we only advance time forward.
                
                # Actually off_free[k] could be < time if that official finished before time
                # and we haven't used them since. So min(new_off) could be < time.
                # But we can't go back in time, so next_time = max(time, min(new_off))? No.
                # We can schedule at min(new_off) if min(new_off) >= time, but if min(new_off) < time,
                # we can schedule at time.
                
                # Actually, the next decision time is max(time, min(new_off))? No.
                # If an official is free at time 3 and current time is 5, we can schedule at 5.
                # If all officials are busy until time 7, we must wait until 7.
                # So next_time = max(time, min(new_off))
                # But min(new_off) could be 0 (if an official was never used), and time is 5,
                # so next_time = 5. That's correct.
                # If min(new_off) is 7 and time is 5, next_time = 7. Correct.
                
                # Wait, but we also need to consider that we might want to schedule
                # at a time between time and end_time. The state (end_time, ...) would
                # miss that. So we need to use next_time = max(time, min(new_off))
                # but this might not be end_time.
                
                # Let me reconsider. The state should be:
                # (current_time, pos, off_free)
                # where current_time is the time we're making decisions.
                # When we schedule doc i on official off:
                #   start_time = max(current_time, off_free[off])
                #   end_time = start_time + dur
                #   new_off[off] = end_time
                #   new_pos[i] += 1
                #   new_current_time = max(current_time, min(new_off))
                #     because we can next make a decision at the earliest time
                #     an official is free, but not before current_time
                #     (since we can't go back)
                #   Actually, new_current_time should be min(new_off) if min(new_off) > current_time
                #   else current_time
                #   = max(current_time, min(new_off))? No, if min(new_off) < current_time,
                #   we use current_time. If min(new_off) > current_time, we use min(new_off).
                #   So new_current_time = max(current_time, min(new_off))? No.
                #   If min(new_off) = 3 and current_time = 5, new_current_time = 5.
                #   If min(new_off) = 7 and current_time = 5, new_current_time = 7.
                #   So new_current_time = max(current_time, min(new_off))? 
                #   max(5, 3) = 5. max(5, 7) = 7. Yes, that works.
                
                # But wait, if min(new_off) = 3 and current_time = 5, it means some official
                # is free at 3, but we're at time 5. We can schedule at 5. Correct.
                # But what if we want to schedule at time 3? We can't, because we're at 5.
                # But how did we get to time 5? We must have scheduled something that
                # made us jump to 5. But if an official was free at 3, we should have
                # scheduled at 3 before jumping to 5.
                # 
                # Actually, the issue is that we might skip over times. Let's think
                # about whether this is correct.
                # 
                # The key insight: we should always schedule at the earliest possible
                # time. So current_time should always be the minimum of all official
                # free times (or 0 initially). When we schedule a review, we update
                # that official's free time, and the new current_time is the new minimum.
                # 
                # But we also need to respect document order. A document's next review
                # can only start after its previous review finishes. But we track that
                # via pos[i] - we only schedule the next review when the previous is done.
                # 
                # Wait, but the start time of a review is max(current_time, off_free[off]).
                # If current_time is the min of all off_free, then off_free[off] >= current_time,
                # so start_time = off_free[off]. That means we always start at the official's
                # free time. But what if the document's previous review finishes later?
                # 
                # Ah, I see the issue. The document's previous review might finish at
                # a time later than off_free[off]. We need to track when each document
                # is ready for its next review.
                # 
                # So the state needs to include doc_ready[i] = when doc i is ready for
                # its next review. Initially all 0.
                # When we schedule doc i's review on official off:
                #   start_time = max(doc_ready[i], off_free[off])
                #   end_time = start_time + dur
                #   new_doc_ready[i] = end_time
                #   new_off_free[off] = end_time
                #   new_current_time = min(new_off_free)  # or something
                # 
                # But this increases the state space. Let me think if there's a simpler way.
                # 
                # Actually, since we always schedule at the earliest possible time,
                # and we use a priority queue with time as the key, we can just use
                # the end_time as the time for the next state. But we need to make
                # sure we don't miss parallel schedules.
                # 
                # Let me try a different approach: use the end_time as the state time,
                # but also allow scheduling at times before end_time by considering
                # all possible next actions at the current time.
                # 
                # Actually, the correct approach is:
                # State: (time, pos, off_free, doc_ready)
                # But doc_ready[i] is the time when doc i's previous review finished.
                # When we schedule doc i's next review:
                #   start_time = max(time, doc_ready[i], off_free[off])
                #   But time should be the current decision point, which is the min of
                #   all off_free and all doc_ready? No, time is just when we're making
                #   the decision.
                # 
                # I think the cleanest approach is:
                # - State: (pos, off_free, doc_ready)
                # - The "time" for the state is max(min(off_free), min(doc_ready))? No.
                # - Actually, the earliest we can schedule anything is min over all
                #   possible (max(doc_ready[i], off_free[off])) for valid (i, off) pairs.
                # 
                # Let me just use a simpler state and be more careful.
                # 
                # State: (pos, off_free, doc_ready)
                # Priority: the earliest time we can make a decision = 
                #   min over all i where pos[i] < len(docs[i]) of max(doc_ready[i], off_free[docs[i][pos[i]][0]])
                # 
                # But this is expensive to compute. Let me just store the time in the state
                # and use a different approach.
                # 
                # Alternative: since the total number of reviews is at most 50, and j, m <= 10,
                # we can afford a larger state space. Let's include doc_ready in the state.
                # 
                # State: (time, pos, off_free, doc_ready)
                # time = current decision time
                # When we schedule doc i:
                #   off, dur = docs[i][pos[i]]
                #   start_time = max(time, doc_ready[i], off_free[off])
                #   end_time = start_time + dur
                #   new_pos[i] += 1
                #   new_off_free[off] = end_time
                #   new_doc_ready[i] = end_time
                #   new_time = ?
                # 
                # For new_time, we want the earliest time we can make a new decision.
                # This is the minimum over all possible next actions of their start_time.
                # But we can just set new_time = end_time and let the priority queue
                # handle it, but we might miss parallel schedules.
                # 
                # Actually, let's think about it differently. The priority queue should
                # always pop the state with the earliest time. When we pop a state,
                # we try all possible next actions. For each action, we compute the
                # start_time and end_time, and push (end_time, new_state). But we also
                # need to allow scheduling other actions at the current time.
                # 
                # The issue is that when we schedule one action, we should also be able
                # to schedule other actions at the same time (if they don't conflict).
                # 
                # One way: when we pop a state at time T, we try all subsets of actions
                # that can start at time T. But this is exponential.
                # 
                # Better way: we don't need to schedule all at once. We can schedule
                # one at a time. When we schedule action A at time T, we create a new
                # state where A is scheduled (ending at T + dur_A), and the new time is
                # still T (so we can schedule more actions at T). But we also create a
                # state where we skip to the next decision time.
                # 
                # Actually, the standard approach for job shop scheduling is:
                # - State: (pos, off_free, doc_ready)
                # - The time is max(min(off_free), min(doc_ready))? No.
                # - Actually, the time is the makespan so far, which is max of all end times.
                # - But we want to minimize the makespan.
                # 
                # Let me try yet another approach. Since the state space is small
                # (pos has at most 50^10 states, but actually much smaller due to
                # total reviews <= 50), we can use a different formulation.
                # 
                # Actually, let's bound the state space. Each doc has at most 50 reviews
                # total, so pos[i] ranges from 0 to len(docs[i]). The number of possible
                # pos tuples is product of (len(docs[i]) + 1), which is at most 51^10 but
                # with total reviews <= 50, it's much smaller.
                # 
                # off_free has m dimensions, each up to some max time. doc_ready has j
                # dimensions. This could be large.
                # 
                # Let me think about the problem differently. Since total reviews <= 50
                # and j, m <= 10, maybe we can use a different approach.
                # 
                # Actually, let's just be more careful with the state. The key insight
                # is that we should always schedule at the earliest possible time.
                # So the state time should be the earliest time we can schedule
                # something, which is min over all valid (i, off) of max(doc_ready[i], off_free[off]).
                # 
                # But we don't need to store time in the state if we compute it from
                # the state. Let's define:
                # 
                # State: (pos, off_free, doc_ready)
                # time(state) = min over all i with pos[i] < len(docs[i]) of max(doc_ready[i], off_free[docs[i][pos[i]][0]])
                # 
                # When we schedule doc i:
                #   off, dur = docs[i][pos[i]]
                #   start = max(doc_ready[i], off_free[off])
                #   end = start + dur
                #   new_pos[i] += 1
                #   new_off_free[off] = end
                #   new_doc_ready[i] = end
                # 
                # The priority is time(state). We use Dijkstra.
                # 
                # But the state space might still be too large because off_free and
                # doc_ready can take many values.
                # 
                # However, since total reviews <= 50 and durations <= 1000, the max
                # time is at most 50 * 1000 = 50000. And m, j <= 10. So off_free has
                # 10 dimensions each up to 50000, which is way too large.
                # 
                # But in practice, the number of reachable states is much smaller.
                # Let's just try it and see.
                # 
                # Actually, let me think about whether we really need doc_ready.
                # 
                # doc_ready[i] is the end time of doc i's last scheduled review.
                # off_free[off] is the end time of official off's last scheduled review.
                # 
                # When we schedule doc i's next review on official off:
                #   start = max(doc_ready[i], off_free[off])
                #   end = start + dur
                # 
                # The key observation: doc_ready[i] and off_free[off] are both end times
                # of previously scheduled reviews. So they're determined by the schedule.
                # 
                # But we can simplify: instead of tracking absolute times, we can note
                # that the relative ordering matters. But this is getting complicated.
                # 
                # Let me just implement the Dijkstra with (pos, off_free, doc_ready)
                # and see if it's fast enough. Given the constraints (total reviews <= 50,
                # j, m <= 10), it should be manageable.
                pass
        
        # I'll implement the full solution below
        pass
    
    # Let me rewrite the solution properly
    pass

def solve2():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    docs = []
    for _ in range(j):
        o = int(next(it))
        seq = []
        for _ in range(o):
            off = int(next(it))
            dur = int(next(it))
            seq.append((off-1, dur))
        docs.append(seq)
    
    # State: (pos_tuple, off_free_tuple, doc_ready_tuple)
    # time = min over all i with pos[i] < len(docs[i]) of max(doc_ready[i], off_free[docs[i][pos[i]][0]])
    # If no such i, time = max of all doc_ready (makespan)
    
    start_pos = tuple(0 for _ in range(j))
    start_off = tuple(0 for _ in range(m))
    start_doc = tuple(0 for _ in range(j))
    start_state = (start_pos, start_off, start_doc)
    
    def compute_time(state):
        pos, off_free, doc_ready = state
        min_start = float('inf')
        for i in range(j):
            if pos[i] < len(docs[i]):
                off, dur = docs[i][pos[i]]
                start = max(doc_ready[i], off_free[off])
                if start < min_start:
                    min_start = start
        if min_start == float('inf'):
            # All done
            return max(doc_ready) if doc_ready else 0
        return min_start
    
    def is_done(state):
        pos, _, _ = state
        for i in range(j):
            if pos[i] < len(docs[i]):
                return False
        return True
    
    visited = {}
    start_time = compute_time(start_state)
    visited[start_state] = start_time
    heap = [(start_time, start_state)]
    
    while heap:
        time, state = heappop(heap)
        if visited.get(state, float('inf')) < time:
            continue
        
        if is_done(state):
            pos, off_free, doc_ready = state
            print(max(doc_ready) if doc_ready else 0)
            return
        
        pos, off_free, doc_ready = state
        for i in range(j):
            if pos[i] < len(docs[i]):
                off, dur = docs[i][pos[i]]
                start = max(doc_ready[i], off_free[off])
                # Only schedule if start == time (earliest possible)
                if start != time:
                    continue
                end = start + dur
                new_pos = list(pos)
                new_pos[i] += 1
                new_pos = tuple(new_pos)
                new_off = list(off_free)
                new_off[off] = end
                new_off = tuple(new_off)
                new_doc = list(doc_ready)
                new_doc[i] = end
                new_doc = tuple(new_doc)
                new_state = (new_pos, new_off, new_doc)
                new_time = compute_time(new_state)
                if new_state not in visited or new_time < visited[new_state]:
                    visited[new_state] = new_time
                    heappush(heap, (new_time, new_state))
    
    # Shouldn't reach here
    print(0)

solve2()