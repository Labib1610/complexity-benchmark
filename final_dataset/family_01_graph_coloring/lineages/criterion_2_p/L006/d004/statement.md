# Problem B — System Equilibrium

Time limit: 1 s   Memory limit: 256 MB

You are tasked with finding a vector $S = \begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n \end{pmatrix}$ such that $s_i \in \{1, 2\}$ for all $1 \le i \le n$, which satisfies the matrix equation:

$$ M S = \mathbf{3} $$

Here, $\mathbf{3}$ is an $m$-dimensional column vector where every element is exactly 3. 

The matrix $M$ has $m$ rows and $n$ columns. It is constructed from a given sequence of $m$ index pairs. Initially, $M$ is a zero matrix. For the $j$-th pair $(u, v)$, we increment the value at row $j$, column $u$ by 1, and we increment the value at row $j$, column $v$ by 1. (Note that if $u = v$, the cell at row $j$, column $u$ is incremented by 2, and no other cells in row $j$ are changed). All other entries in row $j$ remain 0.

If there are multiple valid vectors $S$ that satisfy the equation, you must output the sequence $s_1 \dots s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the pair of indices used to construct the $j$-th row of matrix $M$. The pairs are given in order for $j = 1, 2, \dots, m$.

## Output
If no such vector $S$ exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$) representing the elements of the lexicographically smallest valid vector $S$.

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