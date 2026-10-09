# Problem A — Basis Alignment Procurement

Time limit: 5 s   Memory limit: 256 MB

## Description

You are analyzing an $n$-dimensional vector space over the real numbers with a fixed standard basis $x_1, x_2, \ldots, x_n$. Within this space, a specific set of $t$ basis vectors are designated as objective targets.

You are tasked with procuring a subset of vectors from a provided catalog. Each catalog entry allows you to add the vector $x_u - x_v$ to your chosen subset for a specified procurement expense.

Your goal is to select a subset of the available vectors such that any linear functional $f$ that evaluates to zero on all your selected vectors will necessarily assign the exact same value to all objective targets. 

Calculate the minimum total expense required to procure a subset that satisfies this condition.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ t ≤ 10). The integer **t** is the number of objective targets.
The second line provides **t** distinct integers representing the indices of these objective targets.
The subsequent **m** lines each contain three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), describing a catalog entry that provides the vector $x_u - x_v$ for a procurement expense of **w**.
It is guaranteed that the available options are sufficient to satisfy the condition for all objective targets.

## Output

Print a single integer: the minimum total expense to satisfy the condition for all objective targets.

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

In Example 1, procuring the vectors $x_1 - x_4$, $x_2 - x_4$, and $x_3 - x_4$ incurs a total expense of 1+1+1 = 3. Any linear functional $f$ evaluating to zero on these vectors must satisfy $f(x_1) = f(x_4)$, $f(x_2) = f(x_4)$, and $f(x_3) = f(x_4)$. Consequently, $f(x_1) = f(x_2) = f(x_3)$, meaning $f$ assigns the same value to all three objective targets. This is more economical than selecting a subset of vectors that do not involve $x_4$ (which would cost at least 4).

In Example 3, there is only a single objective target. The condition that $f$ must assign the same value to all objective targets is vacuously satisfied by an empty subset of vectors, resulting in a cost of 0.