for each edge (u, v):
    a = free_color(u)  # smallest color not used at u
    b = free_color(v)  # smallest color not used at v
    if a == b:
        assign color a
    else:
        # assign color a to (u,v), then fix conflicts
        # swap: we recolor edges along an alternating path
        # Let's do: color (u,v) with a. Now at v, color a might conflict with existing edge (x, v) with color a.
        # Recolor (x, v): we want to give it color b (free at v? no, b is free at v originally, but now a is used at v by (u,v)... b is still free at v).
        # So recolor edge (x, v) to color b. But b might conflict at x. Then continue: at x, b might be used by edge (x, y). Recolor (x, y) to... the free color at x, etc.