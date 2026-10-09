# Problem C — Sequence Resonance

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a system of $n$ sequences, denoted $S_1, S_2, \ldots, S_n$. Each sequence has a length of exactly $m$ bits, and all bits are initially set to $0$.

The system's configuration is defined by a list of $m$ operations. For each $k$ from $1$ to $m$, the $k$-th operation specifies two distinct sequence indices $u$ and $v$. This operation modifies the $k$-th position of the sequences by setting $S_u[k] = 1$ and $S_v[k] = 1$. The $k$-th position of all other sequences remains $0$. No two operations will specify the exact same pair of indices $\{u, v\}$.

For any two sequences $S_i$ and $S_j$, we define their pairwise score $F(S_i, S_j)$ as the sum over all $m$ positions of a position score. For position $k$, the score is $3$ if both $S_i[k] = 1$ and $S_j[k] = 1$. Otherwise, the score is $1$.

Your task is to find a "resonance" among the sequences. A resonance is formed by three distinct sequence indices $a$, $b$, and $c$ (with $a < b < c$) such that their pairwise scores satisfy the following equation:

$F(S_a, S_b) + F(S_b, S_c) + F(S_c, S_a) = 3m + 6$

## Input
The first line contains two integers $n$ and $m$. The integer $n$ ($3 \le n \le 2000$) defines the number of sequences. The integer $m$ ($3 \le m \le 200000$) defines the length of each sequence and the number of operations. It is guaranteed that $m \le n(n-1)/2$.

Each of the following $m$ lines corresponds to an operation. For $k$ from $1$ to $m$, the $k$-th of these lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating the sequences modified in operation $k$. 

It is guaranteed that at least one valid resonance exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These integers must form a valid resonance as described above. 

If there are multiple valid trios, output the one that is lexicographically smallest. This means you should output the trio with the smallest value for $a$; if there is a tie, choose the one with the smallest value for $b$; and if a tie remains, choose the one with the smallest value for $c$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```