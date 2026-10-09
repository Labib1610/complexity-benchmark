import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    j = int(input_data[0])
    m = int(input_data[1])
    
    projects = []
    idx = 2
    for _ in range(j):
        o = int(input_data[idx])
        idx += 1
        phases = []
        for _ in range(o):
            f = int(input_data[idx])
            d = int(input_data[idx+1])
            phases.append((f - 1, d))
            idx += 2
        projects.append(phases)
        
    # dp[facility_availability] = min_project_finish_time
    dp = {tuple([0] * m): 0}
    
    for phases in projects:
        new_dp = {}
        for avail, min_finish in dp.items():
            avail_list = list(avail)
            current_start = min_finish
            for f, d in phases:
                current_start = max(current_start, avail_list[f])
                avail_list[f] = current_start + d
                current_start = avail_list[f]
            new_avail = tuple(avail_list)
            new_finish = current_start
            if new_avail not in new_dp or new_finish < new_dp[new_avail]:
                new_dp[new_avail] = new_finish
        dp = new_dp
        
    print(min(dp.values()))

if __name__ == '__main__':
    solve()