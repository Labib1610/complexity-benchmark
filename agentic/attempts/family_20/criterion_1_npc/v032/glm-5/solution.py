solve():
  stack-based DFS from vertex 0:
  state: color[e], used colors per vertex.
  visit vertex v (entered via colored edge e0):
    remaining colors R = {1,2,3} \ {color[e0]}
    other edges of v: e1, e2 (uncolored... or maybe colored if v was touched before)
    ...