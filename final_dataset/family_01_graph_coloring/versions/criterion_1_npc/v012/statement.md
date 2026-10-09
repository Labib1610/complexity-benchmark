# Problem A — Orbital Interference

Time limit: 2 s   Memory limit: 256 MB

A newly deployed satellite carries $n$ scientific instruments. The power distribution system consists of exactly three isolated power buses, designated by the identifiers 1, 2, and 3. To bring the satellite online, every instrument must be connected to exactly one of these three buses.

During testing, engineers discovered that certain pairs of instruments generate electromagnetic interference. If both instruments in such a pair draw power from the same bus, they will malfunction. You are given the complete list of these interfering pairs.

Determine a valid configuration that routes each instrument to a bus such that no two interfering instruments share the same bus. If no such configuration can be achieved, you must report that it is impossible.

## Input
The first line provides two integers $n$ and $m$ — the total number of instruments and the number of interfering pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that instrument $u$ and instrument $v$ will malfunction if connected to the same power bus.

## Output
If there is no valid way to connect all instruments to the three buses safely, print a single line containing the word NO.
If a valid configuration exists, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \ldots, s_n$ separated by spaces, where $s_i \in \{1, 2, 3\}$ is the bus identifier assigned to the $i$-th instrument. Any valid configuration is accepted.

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
