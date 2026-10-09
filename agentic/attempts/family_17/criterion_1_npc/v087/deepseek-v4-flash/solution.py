We need to determine if we can partition the set {1, 2, …, 3q} into q triples, each triple being one of the given blueprints.

This is essentially a **3-dimensional matching** problem, which is NP-hard in general. However, the constraints and the special properties (span < 3q, sum ≤ 9q−3) might allow a greedy or constructive approach.

Let’s think:

- We have exactly 3q components, and each blueprint uses exactly 3 distinct components.
- We need to select q blueprints that are disjoint and cover all components.

This is equivalent to finding a perfect matching in a 3-uniform hypergraph.  
Given q ≤ 200, t ≤ 20000, we can try a backtracking with pruning, but worst-case exponential is too slow.

However, the problem might be solvable by a greedy approach:  
Sort blueprints by their smallest component, and try to pick them in order, skipping those that conflict with already chosen ones.  
But that might fail in some cases.

Another idea: Since the sum constraint is ≤ 9q−3, and span < 3q, maybe the triples are “local” in some sense.  
But we cannot rely on that for correctness.

Given the time limit (5s) and constraints, we can try a **maximum matching** approach using flow or bipartite matching?  
But 3D matching is not reducible to bipartite matching directly.

However, note that q ≤ 200, so the number of components is at most 600.  
We can model this as an exact cover problem and use Algorithm X (Dancing Links) with pruning.  
With t ≤ 20000, but q small, it might be feasible.

Let’s implement a backtracking with:
- Sort blueprints by smallest component.
- Maintain used[] array.
- Recursively pick the smallest unused component, try all blueprints containing it, and recurse.

We can precompute for each component the list of blueprints containing it.

Complexity: In worst case, branching factor could be large, but with q=200, we might still be okay if we prune well.

Let’s code it.

We’ll also need to output the selected triples.

Implementation steps:
1. Read q, t.
2. Store blueprints as tuples (a,b,c).
3. Build adjacency: for each component id (1..3q), list of blueprint indices containing it.
4. Backtracking:
   - used_comp[1..3q] boolean
   - selected list of blueprint indices
   - find first unused component
   - for each blueprint containing it, if all three unused, select it, mark used, recurse.
   - If we select q blueprints, success.
5. If success, print YES and the triples.

We must be careful with recursion depth (q ≤ 200, fine