import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    k = int(input_data[0])
    t = int(input_data[1])
    
    tech_triples = [[] for _ in range(k)]
    rig_triples = [[] for _ in range(k)]
    win_triples = [[] for _ in range(k)]
    
    idx = 2
    for i in range(t):
        x = int(input_data[idx]) - 1
        y = int(input_data[idx+1]) - 1
        z = int(input_data[idx+2]) - 1
        idx += 3
        
        tech_triples[x].append((y, z, i))
        rig_triples[y].append((x, z, i))
        win_triples[z].append((x, y, i))
    
    all_mask = (1 << k) - 1
    solution = []
    
    def dfs(used_x, used_y, used_z):
        if used_x == all_mask:
            return True
        
        min_cnt = 1000000
        best_candidates = None
        
        # Check unused technicians
        for x in range(k):
            if not (used_x & (1 << x)):
                cnt = 0
                cand = []
                for y, z, tid in tech_triples[x]:
                    if not (used_y & (1 << y)) and not (used_z & (1 << z)):
                        cnt += 1
                        cand.append((x, y, z))
                if cnt == 0:
                    return False
                if cnt < min_cnt:
                    min_cnt = cnt
                    best_candidates = cand
                    if min_cnt == 1:
                        break
        
        # Check unused rigs
        if min_cnt > 1:
            for y in range(k):
                if not (used_y & (1 << y)):
                    cnt = 0
                    cand = []
                    for x, z, tid in rig_triples[y]:
                        if not (used_x & (1 << x)) and not (used_z & (1 << z)):
                            cnt += 1
                            cand.append((x, y, z))
                    if cnt == 0:
                        return False
                    if cnt < min_cnt:
                        min_cnt = cnt
                        best_candidates = cand
                        if min_cnt == 1:
                            break
        
        # Check unused windows
        if min_cnt > 1:
            for z in range(k):
                if not (used_z & (1 << z)):
                    cnt = 0
                    cand = []
                    for x, y, tid in win_triples[z]:
                        if not (used_x & (1 << x)) and not (used_y & (1 << y)):
                            cnt += 1
                            cand.append((x, y, z))
                    if cnt == 0:
                        return False
                    if cnt < min_cnt:
                        min_cnt = cnt
                        best_candidates = cand
                        if min_cnt == 1:
                            break
        
        for x, y, z in best_candidates:
            solution.append((x + 1, y + 1, z + 1))
            if dfs(used_x | (1 << x), used_y | (1 << y), used_z | (1 << z)):
                return True
            solution.pop()
        
        return False

    if dfs(0, 0, 0):
        print("YES")
        for x, y, z in solution:
            print(f"{x} {y} {z}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()