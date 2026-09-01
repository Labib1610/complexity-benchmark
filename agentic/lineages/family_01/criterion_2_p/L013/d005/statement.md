# Transformation Network

Time limit: 1 s
Memory limit: 256 MB

A network consists of $n$ nodes. Each node must be assigned exactly one of two mathematical transformation rules:
- Rule 1: $f(x) = -x$
- Rule 2: $f(x) = 1/x$

There are $m$ links in the network. Each link connects two specific nodes $u$ and $v$. A link is considered stable if and only if the composition of the rules assigned to its two endpoints (applied in either order) yields $f_u(f_v(x)) = -1/x$ for all $x \neq 0$. If any link produces a different composition (such as $f_u(f_v(x)) = x$), the link is unstable and the entire configuration is invalid.

Your task is to determine whether there is an assignment of rules (either 1 or 2) to all $n$ nodes such that every link in the network is stable. If multiple valid assignments exist, you must output the one that minimizes the sequence of assigned rule numbers $s_1, s_2, \dots, s_n$ lexicographically.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a link connects node $u$ and node $v$.

## Output
If no stable assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \ldots, s_n$ (each being 1 or 2) representing the lexicographically smallest valid assignment.

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