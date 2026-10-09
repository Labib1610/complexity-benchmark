# Problem B — Harmonized Frequencies

Time limit: 1 s
Memory limit: 256 MB

A manufacturing plant operates $n$ robotic assembly arms. Each arm must be configured to an integer operational mode $s_i$, which must be chosen from the set $\{1, 2\}$. 

The facility has identified $m$ specific pairs of arms that share physical workspace. To avoid collisions, any two arms that share a workspace must pass a joint diagnostic check. The diagnostic system concatenates the operational modes of the two arms to form a two-digit diagnostic code. The check passes if and only if this two-digit code is a multiple of 3. (Whether the system forms the code as $s_u s_v$ or $s_v s_u$, the divisibility result is the same).

Determine a valid operational mode for each assembly arm so that all shared workspace diagnostic checks are passed. If no such configuration exists, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of assembly arms and the number of shared workspace pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of arms that share physical workspace.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$), representing the operational mode assigned to each arm. If multiple valid configurations exist, output the one that is lexicographically smallest.

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