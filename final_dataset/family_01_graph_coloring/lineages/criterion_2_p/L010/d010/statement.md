# Problem B — Differential Routing

Time limit: 1 s
Memory limit: 256 MB

A communications array consists of $n$ transceivers. Each transceiver $i$ must be configured to a fixed voltage level $s_i$, which must be chosen from the set of positive integer divisors of 2 (i.e., each $s_i \in \{1, 2\}$).

The array contains $m$ differential signaling links. To successfully transmit data without interference, each link must be perfectly balanced. The diagnostic system evaluates the balance of any link connecting transceiver $u$ and transceiver $v$. A link is considered balanced if and only if the set of voltage levels assigned to $u$ and $v$ contains both 1 and 2 (meaning one transceiver operates at level 1 and the other at level 2).

Determine a valid voltage level for each transceiver so that all $m$ differential links are balanced. If no such configuration exists, you must report it.

The system requires the configuration to be standardized. If multiple valid configurations exist, you must output the lexicographically smallest sequence $s_1, \dots, s_n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of transceivers and the number of differential links, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — indicating that a differential link connects transceiver $u$ and transceiver $v$.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$), representing the voltage level assigned to each transceiver. If multiple valid configurations exist, output the lexicographically smallest sequence $s_1 \dots s_n$.

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