import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    teams = []
    for _ in range(t):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        teams.append((a,b,c))
    
    # Precompute teams per agent
    agent_teams = [[] for _ in range(3*q+1)]
    for idx, (a,b,c) in enumerate(teams):
        agent_teams[a].append(idx)
        agent_teams[b].append(idx)
        agent_teams[c].append(idx)
    
    used = [False]*(3*q+1)
    chosen = []
    
    def backtrack(count):
        if count == q:
            return True
        # find smallest unused agent
        first = 1
        while first <= 3*q and used[first]:
            first += 1
        if first > 3*q:
            return False
        # try teams containing first
        for tidx in agent_teams[first]:
            a,b,c = teams[tidx]
            if used[a] or used[b] or used[c]:
                continue
            # use this team
            used[a] = used[b] = used[c] = True
            chosen.append((a,b,c))
            if backtrack(count+1):
                return True
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False
    
    if backtrack(0):
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()