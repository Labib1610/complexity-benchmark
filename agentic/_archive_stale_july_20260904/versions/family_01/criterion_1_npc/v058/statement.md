# Problem A — The Tri-Position Lock

Time limit: 2 s   Memory limit: 256 MB

Inside a secure vault door lies a network of $m$ rigid crossbars. Each crossbar bridges a specific pair of rotary dials, of which there are $n$ in total (numbered 1 to $n$). Every individual dial features exactly three distinct settings, labeled 1, 2, and 3.

The shape of the crossbars dictates a strict mechanical limitation: if the two dials bridged by any single crossbar are rotated to the exact same setting, that crossbar will seize and trigger a permanent lockdown. A configuration is only valid if every single crossbar bridges a pair of dials that have differing settings.

You are attempting to open this complex mechanical vault. To achieve this, you must determine a full sequence of settings for all $n$ dials that avoids triggering a lockdown. If the mechanism is inherently impossible to configure without seizing, you must report it. Otherwise, you must provide the configuration that successfully opens the vault.

## Input
The first line contains two integers $n$ and $m$ — the number of dials and the number of crossbars (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n−1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two dials bridged by a crossbar. Dials are identified by integers from 1 to $n$.

## Output
If there is no combination of dial settings that avoids a lockdown, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $p_1, p_2, \dots, p_n$ (each $p_i \in \{1, 2, 3\}$), where $p_i$ is the setting of dial $i$. Among all valid configurations that open the vault, you must output the one that is lexicographically smallest. (A sequence $A$ is lexicographically smaller than sequence $B$ if, at the first index where their settings differ, sequence $A$ has a smaller setting number than sequence $B$).

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
