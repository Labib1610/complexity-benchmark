# Problem C — Triadic Resonance

Time limit: 2 s   Memory limit: 256 MB

A symmetric boolean function $F(x, y)$ evaluates to either $1$ (true) or $0$ (false) for any two integer inputs $x$ and $y$. You are given the complete list of input pairs for which $F(x, y) = 1$. For all other pairs, $F(x, y) = 0$. The function is symmetric, meaning $F(x, y) = F(y, x)$ for all $x$ and $y$, and $F(x, x) = 0$ for all $x$.

Your task is to find a "triadic resonance" in the system. A triadic resonance is formed by three distinct integers $a, b,$ and $c$ that mutually satisfy the function. Specifically, you must find a trio such that:
$F(a, b) = 1$
$F(a, c) = 1$
$F(b, c) = 1$

## Input
The first line contains two integers $n$ and $m$. The integer $n$ ($3 \le n \le 2000$) defines the domain of the inputs; all inputs to $F$ are integers from 1 to $n$. The integer $m$ specifies the number of unordered pairs $\{u, v\}$ for which $F(u, v) = 1$. The value of $m$ is at least 3 and at most 200000, and it will never exceed the maximum possible number of distinct pairs that can be formed from $n$ elements (i.e., $m \le n(n-1)/2$).

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that $F(u, v) = 1$ and $F(v, u) = 1$. 

It is guaranteed that at least one valid triadic resonance exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These integers must form a valid triadic resonance as described above. 

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