Color(G, Δ):
  if Δ = 1: color all edges with color 1.
  if Δ is even:
     split G into G1, G2 via Euler split (each max degree ≤ Δ/2)
     Color(G1, Δ/2); Color(G2, Δ/2) with offset.
  if Δ is odd:
     find a matching M covering all vertices of degree Δ
     color M with color Δ
     Color(G - M, Δ - 1)