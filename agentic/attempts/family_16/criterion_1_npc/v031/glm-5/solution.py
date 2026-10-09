import sys
import heapq

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    
    dishes = []
    for _ in range(j):
        o = int(next(it))
        steps = []
        for _ in range(o):
            ws = int(next(it)) - 1
            dur = int(next(it))
            steps.append((ws, dur))
        dishes.append(steps)
    
    # State: (time, dish_finish_times, workstation_free_times)
    # dish_finish_times: tuple of finish times for each dish (last step finished)
    # workstation_free_times: tuple of times when each workstation becomes free
    
    # Initial state
    init_dish_times = tuple(0 for _ in range(j))
    init_ws_times = tuple(0 for _ in range(m))
    
    pq = [(0, init_dish_times, init_ws_times)]
    visited = {(init_dish_times, init_ws_times)}
    
    while pq:
        t, dish_times, ws_times = heapq.heappop(pq)
        
        # Check if all dishes are complete
        all_done = True
        for i, steps in enumerate(dishes):
            if len(steps) > 0:
                all_done = False
                break
        
        if all_done:
            print(t)
            return
        
        # Generate next states by choosing which dish to advance
        # We can process dishes in any order, but we use a canonical ordering
        # to avoid duplicate states
        
        # Find the minimum time at which any step can start
        # This is max(dish_ready_time, workstation_ready_time)
        
        # For efficiency, we'll try to advance each dish that has remaining steps
        for dish_idx in range(j):
            steps = dishes[dish_idx]
            if len(steps) == 0:
                continue
            
            ws, dur = steps[0]
            dish_ready = dish_times[dish_idx]
            ws_ready = ws_times[ws]
            start_time = max(dish_ready, ws_ready)
            finish_time = start_time + dur
            
            # Create new state
            new_dish_times = list(dish_times)
            new_dish_times[dish_idx] = finish_time
            new_dish_times = tuple(new_dish_times)
            
            new_ws_times = list(ws_times)
            new_ws_times[ws] = finish_time
            new_ws_times = tuple(new_ws_times)
            
            # Create new dishes list (with first step removed)
            new_dishes = list(dishes)
            new_dishes[dish_idx] = steps[1:]
            new_dishes = tuple(new_dishes)
            
            state = (new_dish_times, new_ws_times, new_dishes)
            
            if state not in visited:
                visited.add(state)
                heapq.heappush(pq, (finish_time, new_dish_times, new_ws_times))

if __name__ == "__main__":
    solve()