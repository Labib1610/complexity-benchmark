# Problem B — Network Configuration

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ modules. Each module $k$ (for $1 \le k \le n$) must be assigned a configuration parameter $s_k \in \{1, 2\}$.

These parameters determine the module's internal complex coefficient $c_k$, where $\mathbf{i}$ is the imaginary unit:
- Assignment $s_k = 1$ sets the coefficient $c_k = 3 + 4\mathbf{i}$.
- Assignment $s_k = 2$ sets the coefficient $c_k = 3 - 4\mathbf{i}$.

The system log contains $m$ active connections. Each connection involves two modules $u$ and $v$. 
When a connection is active, the transmission line couples the two modules. To ensure signal stability, the real part of the complex product of their coefficients, $c_u \cdot c_v$, must be strictly positive.

(Note: If a logged connection involves the same module twice, meaning $u = v$, the product is simply the coefficient squared. For both assignment 1 and assignment 2, the square of the coefficient has a real part of $-7$, which immediately violates the stability requirement).

If there are multiple valid state assignments that satisfy all logged connections, you must output the sequence $s_1 \dots s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of the two modules involved in the $j$-th logged connection. The connections are given in order for $j = 1, 2, \dots, m$.

## Output
If no such assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (where each $s_k \in \{1,2\}$) representing the elements of the lexicographically smallest valid assignment.

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