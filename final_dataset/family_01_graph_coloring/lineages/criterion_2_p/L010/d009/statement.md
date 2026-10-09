# Problem B — Harmonized Frequencies

Time limit: 1 s
Memory limit: 256 MB

A manufacturing plant operates $n$ robotic assembly arms. Each arm must be configured to an integer operational mode $s_i$, which must be chosen from the set of positive integer divisors of 2 (i.e., each $s_i \in \{1, 2\}$).

The facility has identified $m$ instances of workspace overlap. To avoid collisions, every overlap must pass a safety check. The diagnostic system evaluates the resonance between any two overlapping arms $u$ and $v$. An overlap is considered safe if and only if the assigned modes satisfy the resonance condition:

$s_u^2 s_v + s_u s_v^2 + s_u^2 + s_v^2 = 11$

Determine a valid operational mode for each assembly arm so that all $m$ safety checks are passed. If no such configuration exists, you must report it.

The plant requires the operational modes to be standardized. If multiple valid configurations exist, you must output the lexicographically smallest sequence $s_1, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of assembly arms and the number of overlaps, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — indicating that the workspace of arm $u$ overlaps with the workspace of arm $v$.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$), representing the operational mode assigned to each arm. If multiple valid configurations exist, output the lexicographically smallest sequence $s_1 \dots s_n$.

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