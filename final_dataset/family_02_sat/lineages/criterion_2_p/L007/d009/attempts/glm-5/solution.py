order = []
visited = [False]*N
for s in range(N):
    if visited[s]: continue
    stack = [s]
    visited[s] = True
    while stack:
        v = stack[-1]
        # find next unvisited neighbor...