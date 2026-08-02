# Chamber Pressure Assignment

Time limit: 2 s   Memory limit: 256 MB

A facility operates $n$ storage chambers numbered $1$ through $n$. Each chamber must be configured with an operating pressure level chosen from $\{1, 2, 3\}$.

There are $m$ pairwise conflict rules. Each rule specifies two distinct chambers $u$ and $v$, requiring that chamber $u$ and chamber $v$ do not operate at the same pressure level (that is, $s_u \neq s_v$).

Find a sequence of pressure assignments $(s_1, s_2, \dots, s_n)$ with $s_i \in \{1, 2, 3\}$ for all chambers such that all $m$ conflict rules are satisfied simultaneously. If valid assignments exist, choose the sequence that is lexicographically smallest. Otherwise, indicate that no valid configuration is possible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le \frac{n(n-1)}{2}$), representing the number of chambers and the number of conflict rules, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), defining a conflict rule between chamber $u$ and chamber $v$.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$, where $s_i \in \{1, 2, 3\}$ is the pressure level assigned to chamber $i$, choosing the lexicographically smallest sequence among all valid assignments.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```