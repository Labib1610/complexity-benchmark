# Radio Spectrum Allocation Protocol

Time limit: 2 s   Memory limit: 256 MB

A central telecommunication hub manages $n$ broadcast units, indexed from $1$ to $n$. System diagnostics have identified $m$ distinct pairs of units whose transmissions interfere if they operate on identical channels.

To eliminate interference, each unit must be configured to use one of three distinct baseline operational frequencies, designated by the integers $1$, $2$, and $3$. No two interfering units may share the same frequency setting.

If a valid configuration exists, the hub must apply the configuration sequence $s_1, s_2, \dots, s_n$ that appears first in lexicographical order (comparing $s_1$ first, then $s_2$, and so on) to ensure predictable downstream initialization. If no configuration satisfies all interference constraints, the protocol must report failure.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, where $n$ is bounded above by the 40-slot limit of the hub's backplane, and $0 \le m \le \frac{n(n-1)}{2}$) — representing the number of broadcast units and the number of interfering pairs.
Each of the following $m$ lines contains two distinct integers $u$ and $v$ ($1 \le u, v \le n$), indicating an interference conflict between unit $u$ and unit $v$.

## Output
If no valid assignment exists, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers $s_1 \ s_2 \ \dots \ s_n$ ($s_i \in \{1, 2, 3\}$), denoting the frequency assigned to unit $i$. If multiple valid configurations exist, output the one that is lexicographically smallest.

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
