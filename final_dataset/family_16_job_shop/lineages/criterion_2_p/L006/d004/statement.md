# Problem B — Linear Structure Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

You are assembling a linear composite structure using **j** components. Each component consists of a primary segment of length **p1** and a secondary segment of length **p2**.

You must arrange all **j** components into a single sequence. Let the chosen permutation place the components into positions $1, 2, \dots, j$, where $p1_i$ and $p2_i$ are the lengths for the component assigned to position $i$.

The layout of the structure is completely defined by two sequences of coordinates along an axis: the primary endpoints $X_i$ and the secondary endpoints $Y_i$. These are calculated using the following deterministic recurrences:
- The starting coordinates are $X_0 = 0$ and $Y_0 = 0$.
- For each position $i$ from $1$ to $j$:
  - The primary endpoint is $X_i = X_{i-1} + p1_i$.
  - The secondary segment for position $i$ begins at the maximum of $X_i$ and $Y_{i-1}$. Its endpoint is therefore $Y_i = \max(X_i, Y_{i-1}) + p2_i$.

No other spatial constraints or physical rules apply; only these coordinate recurrences define the layout and the objective.

Find a permutation of the components that makes the final secondary endpoint $Y_j$ as small as possible. Report this minimum possible value of $Y_j$.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the primary length and the secondary length of a component.

## Output

Print a single integer: the minimum possible value of the final secondary endpoint $Y_j$.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 1, an optimal arrangement places the components in the order of the 3rd, 2nd, and 1st from the input.
- For the 3rd input component ($p1=1, p2=3$) at position 1: $X_1 = 0 + 1 = 1$. $Y_1 = \max(1, 0) + 3 = 4$.
- For the 2nd input component ($p1=2, p2=4$) at position 2: $X_2 = 1 + 2 = 3$. $Y_2 = \max(3, 4) + 4 = 8$.
- For the 1st input component ($p1=3, p2=2$) at position 3: $X_3 = 3 + 3 = 6$. $Y_3 = \max(6, 8) + 2 = 10$.
The final secondary endpoint $Y_3$ is 10.