# Problem B — Phase Calibration

Time limit: 1 s   Memory limit: 256 MB

A complex network of $n$ quantum sensors must be calibrated. Each sensor $i$ requires a phase alignment parameter $s_i \in \{1, 2\}$. The calibration space consists of $2^n$ possible joint phase assignments.

Due to quantum entanglement, certain pairs of sensors exhibit phase interference. You are provided with a list of $m$ entangled pairs. For any pair $(u, v)$ in this list, if both sensors are assigned the exact same phase parameter (i.e., $s_u = s_v$), the network experiences a critical collapse. 

Your task is to evaluate the $2^n$-size state space to determine if there is at least one joint phase assignment that satisfies all $m$ interference constraints simultaneously. If no such assignment exists anywhere in the configuration space, you must report this impossibility. Because the calibration system requires deterministic behavior, if multiple valid assignments exist, you must output the one that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of sensors and the number of entangled pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ — an entangled pair.

## Output
If the entire space of $2^n$ assignments contains no valid state, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the valid joint phase assignment that is lexicographically smallest.

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
