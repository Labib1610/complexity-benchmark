# Parameter Unification Cost

Time limit: 5 s   Memory limit: 256 MB

## Description

A computational model relies on a configuration vector of **n** scalar parameters, indexed 1 through $n$. Within this model, **t** specific critical parameters must be guaranteed to hold identical values in every valid configuration.

To restrict the configuration space, you can select from a predefined set of **m** zero-difference conditions. The $i$-th available condition, if selected, enforces that parameter $u$ and parameter $v$ must have a difference of exactly zero. Selecting this condition incurs a fixed performance penalty $w$.

When multiple zero-difference conditions are selected, their effects compound logically. For instance, if conditions enforcing zero difference between parameter $a$ and $b$, and between $b$ and $c$, are both selected, it is mathematically guaranteed that parameter $a$ and $c$ also have zero difference. You are permitted to select conditions involving any parameters, including those that are not among the critical parameters, as long as the selected conditions collectively guarantee that all **t** critical parameters evaluate to the identical value.

Determine the minimum total performance penalty incurred by selecting a subset of these conditions such that, for every configuration vector satisfying the selected conditions, the **t** critical parameters are mathematically guaranteed to be equal.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the indices of the critical parameters.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): an available zero-difference condition between parameter $u$ and parameter $v$ with a performance penalty of $w$.
The provided set of conditions is sufficient to ensure all critical parameters are equal.

## Output

Print a single integer: the minimum total performance penalty to ensure all critical parameters are equal.

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

In Example 1, selecting the conditions involving parameter 4 (between 1 and 4, 2 and 4, and 3 and 4 at a penalty of 1+1+1 = 3) ensures that critical parameters 1, 2, and 3 have zero difference among them. This incurs a lower penalty than selecting the conditions directly between the critical parameters. In Example 3, there is only one critical parameter, so no conditions need to be selected and the minimum penalty is 0.