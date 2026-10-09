# Orbital Instrument Configuration

Time limit: 2 s   Memory limit: 256 MB

A new research satellite is being prepared for launch. It will carry $n$ scientific instruments. To accommodate these devices, the satellite is equipped with three distinct structural booms, labeled 1, 2, and 3. Every instrument must be securely mounted to exactly one of these booms.

During testing, engineers discovered that certain pairs of instruments generate mutual electromagnetic interference. To prevent corrupted readings, any two instruments that interfere with each other must be mounted on different booms. Because there are three booms available, separating an interfering pair still leaves multiple valid mounting options for both instruments.

Your task is to determine whether it is possible to assign each of the $n$ instruments to one of the three booms such that no two interfering instruments end up on the same boom.

## Input
The first line contains two integers $n$ and $m$ — the number of instruments and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that instrument $u$ and instrument $v$ interfere with each other and cannot be mounted on the same boom.

## Output
If no interference-free configuration is possible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $b_1, b_2, \dots, b_n$ separated by spaces, where $b_i \in \{1, 2, 3\}$ represents the boom to which instrument $i$ is assigned. If there are multiple valid configurations, any valid configuration is accepted.

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
