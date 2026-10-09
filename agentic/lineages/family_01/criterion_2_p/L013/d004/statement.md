# Problem B — Matrix Transformation

Time limit: 1 s   Memory limit: 256 MB

You are analyzing a sparse matrix $A$ of dimensions $m \times n$. Every element in $A$ is either 0 or 1. You are given that each of the $m$ rows contains exactly two 1s, with all other elements in the row being 0.

Your objective is to find a column vector $S$ of length $n$ that satisfies two conditions:
1. Every element $s_i$ of $S$ is chosen from the set $\{1, 2\}$.
2. The matrix-vector product $A S$ yields a column vector of length $m$ in which every element is exactly 3.

If such a vector $S$ exists, you must output it. In cases where multiple valid vectors exist, you must choose the one whose sequence of elements $s_1, s_2, \dots, s_n$ is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of columns and the number of rows of the matrix $A$.
The following $m$ lines each contain two integers $u$ and $v$, specifying the 1-based column indices of the two 1s in that row of $A$.

## Output
If no vector $S$ can satisfy the equation $A S = \mathbf{3}$ under the given constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$) denoting the elements of the vector $S$. If there are multiple valid vectors, output the sequence that is lexicographically smallest.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```