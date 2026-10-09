# Problem A — Translation Syndicate

Time limit: 5 s   Memory limit: 256 MB

## Description

A linguistic research team is analyzing **n** historical dialects, numbered 1 through **n**. Their objective is to implement a unified translation framework exclusively for a core subset of **t** focal dialects. 

To facilitate this, the team can hire from a roster of **m** available bilingual experts. Every expert is fluent in exactly two dialects and demands a specific funding amount for their services. 

The framework is considered successful if any two focal dialects can exchange information. This requires that for every pair of focal dialects $A$ and $B$, there is a valid sequence of dialects $D_1, D_2, \dots, D_k$ where:
- $D_1 = A$
- $D_k = B$
- For each step $1 \le i < k$, a hired expert is fluent in both $D_i$ and $D_{i+1}$.

Because expert capabilities are symmetric and funding requirements are always positive, one might initially consider just finding the cheapest independent sequence of experts between each pair of focal dialects. However, whenever multiple translation sequences utilize the exact same expert, that expert's funding is only paid once. Consequently, routing translations through common intermediate dialects—even non-focal ones—can drastically reduce overall costs.

Given that the number of focal dialects **t** is very small, calculate the absolute minimum total funding necessary to hire a group of experts that unifies all focal dialects.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists **t** distinct integers representing the identifiers of the focal dialects.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000). This indicates an available expert fluent in dialects **u** and **v** who requires a funding amount of **w**.
It is guaranteed that a valid group of experts can always be formed to unify the focal dialects.

## Output

Output a single integer representing the minimum total funding required.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In the first example, hiring the experts who bridge dialects (1, 4), (2, 4), and (3, 4) costs 1+1+1 = 3. This allows the focal dialects 1, 2, and 3 to translate between each other via dialect 4. This shared route is cheaper than hiring experts to translate between the focal dialects directly (which would cost 4). 
In the third example, there is only one focal dialect, meaning no experts need to be hired.
