import sys
from heapq import heappush, heappop

def can_finish(projects, m, max_time):
    # projects: list of list of (facility, duration)
    j = len(projects)
    # For each project: next phase index
    next_phase = [0] * j
    # Earliest start time for each project's next phase
    earliest = [0] * j
    # Facility availability time
    facility_free = [0] * (m + 1)
    
    # Min-heap of (start_time, project_idx)
    heap = []
    for i in range(j):
        if next_phase[i] < len(projects[i]):
            heappush(heap, (earliest[i], i))
    
    while heap:
        start, p = heappop(heap)
        if start > max_time:
            return False
        phase_idx = next_phase[p]
        fac, dur = projects[p][phase_idx]
        # Start time is max(earliest[p], facility_free[fac])
        actual_start = max(start, facility_free[fac])
        if actual_start + dur > max_time:
            return False
        finish = actual_start + dur
        facility_free[fac] = finish
        next_phase[p] += 1
        if next_phase[p] < len(projects[p]):
            earliest[p] = finish
            heappush(heap, (finish, p))
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idx = 0
    j = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    projects = []
    for _ in range(j):
        o = int(data[idx]); idx += 1
        phases = []
        for _ in range(o):
            fac = int(data[idx]); idx += 1
            dur = int(data[idx]); idx += 1
            phases.append((fac, dur))
        projects.append(phases)
    
    lo = 0
    hi = sum(dur for proj in projects for _, dur in proj) + 1000
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(projects, m, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    main()