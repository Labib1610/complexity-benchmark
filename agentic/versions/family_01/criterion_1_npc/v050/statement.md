# Problem A — Protocol Synchronization

Time limit: 2 s   Memory limit: 256 MB

A research facility is stabilizing $n$ organic samples. Each sample requires an environmental setting to prevent decay. Specifically, for each sample $i$, you must assign an integer configuration code $c_i$ satisfying $1 \le c_i \le 3$.

Certain samples have conflicting chemical signatures. If two conflicting samples are assigned the identical configuration code, their combined resonance will cause a containment breach. You are provided with the complete registry of these conflicts.

Your task is to determine if every sample can be configured without causing a breach. If it is possible, you must output the exact configuration. In cases where more than one safe configuration exists, the facility's automated logging system enforces a tie-breaking rule: it strictly favors lower configuration codes, prioritized by sample ID. That is, it selects the valid configuration that minimizes the code for sample 1; if multiple valid configurations achieve this minimum, it considers only those and selects the one that minimizes the code for sample 2, and so forth, down to sample $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of organic samples and the number of conflict records. The samples are indexed from 1 to $n$.
The subsequent $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that sample $u$ and sample $v$ have conflicting chemical signatures and must not share the same configuration code.

## Output
If there is no configuration that avoids a breach, output `NO` on a single line.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $c_1, c_2, \dots, c_n$, where $c_i$ is the configuration code for sample $i$. This sequence must be the one selected by the automated logging system's tie-breaking rule.

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
