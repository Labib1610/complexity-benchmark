# Problem B — Orbital Relays

Time limit: 1 s   Memory limit: 256 MB

A communications network is formed by $n$ orbital relays, indexed from 1 to $n$. Every relay must be equipped with one of two specific hardware configurations, represented by the integers 1 and 2.

The system contains $m$ interference zones. Each zone corresponds to a region of space where the signals from two particular relays overlap. To maintain stable communications, you must enforce a strict safety rule for any pair of relays whose signals overlap: the sum of their assigned configuration integers must be exactly 3. 

Determine a valid hardware assignment for all $n$ relays that satisfies this rule across every interference zone. If no such assignment is possible, you must report the failure.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of relays and the number of interference zones.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), denoting that the signals of relay $u$ and relay $v$ overlap in an interference zone.

## Output
If the relays cannot be safely equipped, output a single line containing NO.
If a valid assignment exists, output YES on the first line. On the second line, output $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1, 2\}$), providing the lexicographically smallest sequence of configurations that fulfills the safety rule.

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