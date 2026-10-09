# Problem B — Network Configuration

Time limit: 1 s   Memory limit: 256 MB

You are configuring a network of $n$ modules. Each module $i$ must be assigned an operational state $s_i \in \{1, 2\}$.

The system log contains $m$ active connections. Each connection involves two modules $u$ and $v$. 
To ensure safe data transfer without collision, the states of the modules on each connection must be completely orthogonal at the bit level. Specifically, the bitwise AND of their operational states ($s_u \ \& \ s_v$) must evaluate to exactly 0.

(Note: If a logged connection involves the same module twice, meaning $u = v$, the bitwise AND of its state with itself is $s_u$, which is either 1 or 2. This can never be 0, immediately violating the requirement and destabilizing the network).

If there are multiple valid state assignments that satisfy all logged connections, you must output the sequence $s_1 \dots s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of the two modules involved in the $j$-th logged connection. The connections are given in order for $j = 1, 2, \dots, m$.

## Output
If no such assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$) representing the elements of the lexicographically smallest valid assignment.

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