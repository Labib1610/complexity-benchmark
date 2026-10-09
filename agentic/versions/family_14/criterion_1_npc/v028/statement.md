# Problem A — Translation Syndicate

Time limit: 5 s   Memory limit: 256 MB

## Description

A linguistic research team is studying **n** distinct historical dialects (identified by integers from 1 to **n**). The team's primary goal is to establish a unified translation framework for a specific subset of **t** focal dialects.

To achieve this, the team can employ bilingual experts. There are **m** experts available. Each expert is proficient in exactly two dialects and requires a specific funding amount to be hired. 

A set of hired experts successfully unifies the focal dialects if, for any two focal dialects $A$ and $B$, information can be translated between them. Information can be translated between $A$ and $B$ if there exists a sequence of dialects $D_1, D_2, \dots, D_k$ such that:
- $D_1 = A$
- $D_k = B$
- For every $1 \le i < k$, at least one hired expert is proficient in both $D_i$ and $D_{i+1}$.

You may hire experts whose proficiencies include dialects outside the **t** focal ones, as long as they contribute to a valid sequence of translations.

Find the minimum total funding required to hire a group of experts that unifies all **t** focal dialects.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the focal dialects.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that an available expert is proficient in dialects **u** and **v**, and requires **w** in funding.
It is guaranteed that it is possible to unify all focal dialects using the available experts.

## Output

Print a single integer: the minimum total funding required.

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

In Example 1, hiring the experts who bridge dialects (1, 4), (2, 4), and (3, 4) costs 1+1+1 = 3. This allows the focal dialects 1, 2, and 3 to translate between each other via dialect 4, which is cheaper than hiring experts to translate between the focal dialects directly (which would cost 4). 
In Example 3, there is only one focal dialect, so no experts need to be hired.
