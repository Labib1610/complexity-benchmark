import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    j = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    components = []
    for _ in range(j):
        o = int(data[idx])
        idx += 1
        tests = []
        for _ in range(o):
            facility = int(data[idx])
            idx += 1
            duration = int(data[idx])
            idx += 1
            tests.append((facility, duration))
        components.append(tests)
    
    # We'll use backtracking with memoization
    # State: for each component, how many tests have been completed
    # For each facility, when it becomes free
    
    # Let's try a different approach: simulate the process
    # Keep track of when each component's next test can start
    # And when each facility is free
    
    # comp_next_test[i] = index of next test for component i, or None if done
    comp_next_test = [0] * j
    # comp_earliest_start[i] = earliest time component i can start its next test
    comp_earliest_start = [0] * j
    # facility_free[f] = earliest time facility f is free (1-based)
    facility_free = [0] * (m + 1)
    
    # To determine when all are done
    total_tests = sum(len(c) for c in components)
    tests_completed = 0
    
    # We need to simulate the process step by step
    # At each step, find a test that can start now
    
    while tests_completed < total_tests:
        # Find the earliest time any test can start
        min_time = float('inf')
        candidate = None  # (comp_index, test_index, start_time)
        
        for i in range(j):
            if comp_next_test[i] < len(components[i]):
                test_idx = comp_next_test[i]
                facility, duration = components[i][test_idx]
                # This test can start at max(comp_earliest_start[i], facility_free[facility])
                start_time = max(comp_earliest_start[i], facility_free[facility])
                if start_time < min_time:
                    min_time = start_time
                    candidate = (i, test_idx, start_time, facility, duration)
        
        if candidate is None:
            break
            
        comp_i, test_idx, start_time, facility, duration = candidate
        end_time = start_time + duration
        
        # Execute this test
        comp_next_test[comp_i] += 1
        tests_completed += 1
        facility_free[facility] = end_time
        if comp_next_test[comp_i] < len(components[comp_i]):
            comp_earliest_start[comp_i] = end_time
        else:
            comp_earliest_start[comp_i] = -1  # Done
    
    # The answer is the maximum time any facility is busy until
    result = max(facility_free)
    print(result)

solve()