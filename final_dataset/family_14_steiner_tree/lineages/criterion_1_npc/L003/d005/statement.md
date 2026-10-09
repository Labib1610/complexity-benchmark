# Problem A — Subspace Spanning Optimization

Time limit: 5 s   Memory limit: 256 MB

## Description

Consider the standard basis vectors $e_1, e_2, \ldots, e_n$ in $\mathbb{R}^n$. 

You are given a target set of $t$ distinct indices from $\{1, \dots, n\}$. Your goal is to construct a subspace $W$ such that for any two indices $x$ and $y$ in the target set, the difference vector $e_x - e_y$ is contained in $W$.

To construct $W$, you may select from a provided list of $m$ candidate vectors. Each candidate vector is of the form $e_u - e_v$ for some $u \neq v$, and selecting it adds it to a chosen set $S$. The subspace $W$ is then defined as the linear span of $S$. Each candidate vector has an associated inclusion cost. 

Determine the minimum possible total cost of a selected set $S$ such that its span $W$ satisfies the target condition. 

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers: the indices in the target set.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$): a candidate vector $e_u - e_v$ available for selection, which has an inclusion cost of $w$.
It is guaranteed that selecting all $m$ candidate vectors generates a subspace that satisfies the condition for the target set.

## Output

Print a single integer: the minimum total cost of a selected set of candidate vectors whose span satisfies the condition.

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

In Example 1, selecting the candidate vectors $e_1 - e_4$, $e_2 - e_4$, and $e_3 - e_4$ (total cost $1+1+1 = 3$) forms a subspace $W$. The difference between any two target basis vectors (for instance, $e_1 - e_2$) is contained in $W$. This selection is more cost-effective than selecting the differences directly between the target indices (which would cost 4). 
In Example 3, with only one index in the target set, no pairwise condition needs to be enforced, so the minimum cost is 0.