# Problem C — Coordinate Configuration Impossibility

Time limit: 2 s   Memory limit: 256 MB

## Description

You are analyzing a system that attempts to generate two sets of 2D coordinates, $S_1$ and $S_2$, on a grid with $j$ rows (indexed $1$ to $j$) and $T$ columns (indexed $1$ to $T$). 

For each row $i$ (from $1$ to $j$), the system is given two target integers, $p_{i,1}$ and $p_{i,2}$. A valid configuration of $S_1$ and $S_2$ must satisfy three rules:

1. **Row Cardinality:** $S_1$ must contain exactly $p_{i,1}$ distinct coordinates in row $i$. $S_2$ must contain exactly $p_{i,2}$ distinct coordinates in row $i$. (A coordinate in row $i$ has the form $(i, x)$ where $1 \le x \le T$).
2. **Column Sparsity:** For any column $k \in \{1 \dots T\}$, $S_1$ can contain at most one coordinate in column $k$. Similarly, $S_2$ can contain at most one coordinate in column $k$. ($S_1$ and $S_2$ are evaluated independently; they may both have a coordinate in the same column $k$).
3. **Strict Abscissa Precedence:** For any given row $i$, if $(i, x) \in S_1$ and $(i, y) \in S_2$, the column index $x$ must be strictly less than the column index $y$.

You are debugging logs from generation failures where a valid configuration is mathematically impossible. For every provided test case, you are guaranteed that exactly one of the following isolated conditions is the root cause. Output the code for the one that applies:
- `JOB i` — Row **i** (1-indexed) cannot be satisfied. It is mathematically impossible to satisfy Row Cardinality and Strict Abscissa Precedence for this row alone within the $T$ available columns, even if we completely ignore Column Sparsity and all other rows.
- `LOAD c` — Set **c** (where **c** $\in \{1, 2\}$) is over-constrained. It is mathematically impossible to satisfy Row Cardinality and Column Sparsity for set $S_c$ alone across all rows within the $T$ available columns, even if we completely ignore Strict Abscissa Precedence and the other set.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the following **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the required number of coordinates $p_{i,1}$ for $S_1$ and $p_{i,2}$ for $S_2$ in row $i$, respectively.

## Output

Print a single line containing the applicable certificate: either `JOB i` or `LOAD c`.

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```