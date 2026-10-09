import sys

def can_finish(projects, m, limit):
    # projects: list of list of (facility, duration)
    # facility_available_time: when each facility becomes free
    facility_free = [0] * (m + 1)
    
    for project in projects:
        current_time = 0
        for fac, dur in project:
            start = max(current_time, facility_free[fac])
            end = start + dur
            if end > limit:
                return False
            facility_free[fac] = end
            current_time = end
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    m = int(next(it))
    projects = []
    total_duration = 0
    for _ in range(j):
        o = int(next(it))
        phases = []
        for _ in range(o):
            fac = int(next(it))
            dur = int(next(it))
            phases.append((fac, dur))
            total_duration += dur
        projects.append(phases)
    
    lo = 0
    hi = total_duration  # upper bound: all phases sequential
    while lo < hi:
        mid = (lo + hi) // 2
        if can_finish(projects, m, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

if __name__ == "__main__":
    main()