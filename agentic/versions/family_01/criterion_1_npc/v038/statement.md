# Problem A — Frequency Allocation

Time limit: 2 s   Memory limit: 256 MB

A network consists of $n$ broadcasting devices. To ensure proper operation, each device must be tuned to exactly one of three available frequency bands, designated by the integers 1, 2, and 3.

Certain devices are situated too close to one another. If two such devices operate on the identical frequency band, they will cause signal degradation. You are provided with a list of all such interfering links. You must determine a configuration that allocates a frequency band to each device such that no two linked devices share the same band. If no such configuration can be formed, you must indicate that it is impossible.

Due to the deployment area's geometry, the total sum of interfering links across all individual devices (counting each link twice, once for each device involved) is strictly bounded and will never exceed $n(n-1)$. Furthermore, no device can be linked to itself.

## Input
The first line provides two integers $n$ and $m$ — the number of devices and the number of interfering links ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ — two devices that will degrade each other's signals if they use the same frequency band.

## Output
If a valid configuration cannot be found, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ represents the frequency band assigned to device $i$. If multiple configurations avoid all signal degradation, you must output the one that minimizes the sequence $s_1, s_2, \dots, s_n$ when compared element by element starting from the first device (i.e., at the first position where two valid sequences differ, the one with the smaller band number must be chosen).

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
