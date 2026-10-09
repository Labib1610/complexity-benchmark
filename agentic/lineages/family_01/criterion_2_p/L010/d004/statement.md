# Problem B — Harmonized Frequencies

Time limit: 1 s
Memory limit: 256 MB

A manufacturing plant operates $n$ robotic assembly arms. Each arm must be configured to an integer operational mode $s_i$, which must be chosen from the set $\{1, 2\}$. 

The facility has identified $m$ instances of directional workspace overlap. To avoid collisions, every overlap must pass a one-way diagnostic check. The diagnostic system evaluates an overlap from arm $u$ into the operating zone of arm $v$ using an asymmetric verification protocol. It concatenates the operational mode of the intruding arm ($s_u$) and the receiving arm ($s_v$) to form a two-digit diagnostic code $s_u s_v$. The overlap is considered safe if and only if this specific two-digit code is a multiple of 3. Because the protocol is directional, the system strictly evaluates the code $s_u s_v$ in that exact order.

Determine a valid operational mode for each assembly arm so that all $m$ directional diagnostic checks are passed. If no such configuration exists, you must report it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of assembly arms and the number of directional overlaps, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating that the workspace of arm $u$ overlaps into the zone of arm $v$.

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