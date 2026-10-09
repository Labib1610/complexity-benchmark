def dinic(s, t):
    flow = 0
    while bfs(s, t):
        while (f := dfs(s, t, INF)):
            flow += f
    return flow