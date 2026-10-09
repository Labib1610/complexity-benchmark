import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(5000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    triplets = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        triplets.append((a, b, c))
        idx += 3
        
    N = 3 * q
    cand = [[] for _ in range(N + 1)]
    for i, (a, b, c) in enumerate(triplets):
        cand[a].append(i)
        cand[b].append(i)
        cand[c].append(i)
        
    for i in range(1, N + 1):
        if not cand[i]:
            print("NO")
            return

    covered = [False] * (N + 1)
    uncovered = set(range(1, N + 1))
    solution = []

    def backtrack():
        if not uncovered:
            return True
        
        best_u = -1
        best_count = 1000000
        best_trips = []
        
        for u in uncovered:
            valid = []
            for tr_idx in cand[u]:
                a, b, c = triplets[tr_idx]
                if not covered[a] and not covered[b] and not covered[c]:
                    valid.append(tr_idx)
            cnt = len(valid)
            if cnt < best_count:
                best_count = cnt
                best_u = u
                best_trips = valid
                if cnt <= 1:
                    break
                    
        if best_count == 0:
            return False
            
        for tr_idx in best_trips:
            a, b, c = triplets[tr_idx]
            if covered[a] or covered[b] or covered[c]:
                continue
            covered[a] = covered[b] = covered[c] = True
            uncovered.remove(a)
            uncovered.remove(b)
            uncovered.remove(c)
            solution.append(tr_idx)
            
            if backtrack():
                return True
                
            solution.pop()
            uncovered.add(a)
            uncovered.add(b)
            uncovered.add(c)
            covered[a] = covered[b] = covered[c] = False
            
        return False

    if backtrack():
        print("YES")
        for tr_idx in solution:
            a, b, c = triplets[tr_idx]
            print(f"{a} {b} {c}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()