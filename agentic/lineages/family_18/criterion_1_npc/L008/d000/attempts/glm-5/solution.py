import sys
  
  def solve():
      data = sys.stdin.buffer.read().split()
      n = int(data[0]); m = int(data[1]); B = int(data[2])
      # read edges
      weights = {}  # (min,max) -> weight
      idx = 3
      for _ in range(m):
          u = int(data[idx])-1; v = int(data[idx+1])-1; idx += 2
          if u == v: continue
          if u > v: u, v = v, u
          weights[(u,v)] = weights.get((u,v), 0) + 1
      ...