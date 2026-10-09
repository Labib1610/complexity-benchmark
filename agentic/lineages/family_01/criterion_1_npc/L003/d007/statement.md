# Antenna Alignment

Time limit: 2 s   Memory limit: 256 MB

You are deploying a network of $n$ communication antennas. Each antenna must be configured with one of three polarization modes, represented by the numeric codes 1, 2, and 3. Every antenna must receive exactly one mode assignment.

There are $m$ pairs of antennas that are in direct line-of-sight of each other. If two antennas in line-of-sight operate on the same polarization mode, their signals will interfere and cause a network failure. Therefore, to ensure stable communication, any two antennas that are in line-of-sight must be assigned different polarization modes.

You must determine whether it is possible to assign a valid polarization mode to all $n$ antennas such that no two line-of-sight antennas share the same mode.

## Input
The first line contains two integers $n$ and $m$ — the number of antennas and the number of line-of-sight pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The antennas are indexed from $1$ to $n$.
Each of the subsequent $m$ lines contains two distinct integers $u$ and $v$ ($1 \le u, v \le n$), indicating that antenna $u$ and antenna $v$ are in line-of-sight. Every listed pair represents a strict interference constraint.

## Output
If a safe configuration is impossible, output a single line containing NO.
If a valid configuration exists, output YES on the first line. On the second line, output $n$ space-separated integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the polarization mode assigned to antenna $i$. Any valid configuration will be accepted.

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