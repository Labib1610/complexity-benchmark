# Antenna Alignment

Time limit: 2 s   Memory limit: 256 MB

You are tasked with configuring a network of $n$ communication antennas. Every antenna in the network requires exactly one operational mode, which must be selected from the numeric codes 1, 2, and 3.

The terrain contains $m$ direct line-of-sight links between specific pairs of antennas. When two antennas share a line-of-sight link, their transmitted signals interact. If the product of the numeric codes assigned to these two linked antennas results in a perfect square, the interaction produces a destructive standing wave that destabilizes the network. To guarantee reliable communication, you must ensure that for every line-of-sight link, the product of the two antennas' operational codes is not a perfect square.

Your objective is to determine if there exists a complete assignment of operational modes to all $n$ antennas that avoids creating any destructive standing waves across the $m$ specified links.

## Input
The first line contains two integers $n$ and $m$ — the number of antennas and the number of line-of-sight links ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The antennas are indexed from $1$ to $n$.
Each of the subsequent $m$ lines provides two distinct integers $u$ and $v$ ($1 \le u, v \le n$), indicating that antenna $u$ and antenna $v$ share a direct line-of-sight link. Each pair represents a strict standing wave constraint.

## Output
If a safe configuration is impossible, output a single line containing NO.
If a valid configuration exists, output YES on the first line. On the second line, output $n$ space-separated integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the operational mode assigned to antenna $i$. Any valid configuration will be accepted.

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