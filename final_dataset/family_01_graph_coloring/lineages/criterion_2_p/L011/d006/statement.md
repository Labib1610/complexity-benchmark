# Harmonic Interference Resolution

Time limit: 1 s
Memory limit: 256 MB

A research facility operates a network of acoustic projectors. To maintain operational stability, every projector in the network (indexed from 1 to $n$) must be assigned a fixed pulse cycle of either 1 microsecond or 2 microseconds.

The facility's layout contains multiple interference thresholds, each connecting a specific pair of projectors. For the network assignment to be viable, any two projectors connected by an interference threshold must be assigned different pulse cycles. A configuration is only valid if this condition is satisfied across every threshold in the entire network.

Your objective is to determine if a viable cycle assignment exists. If multiple valid assignments are possible, you must output the lexicographically smallest sequence of $n$ pulse cycles. This means strictly prioritizing the 1-microsecond cycle for lower-indexed projectors: projector 1 must be assigned 1 if any valid assignment allows it, and subject to that, projector 2 must be assigned 1 if possible, continuing this sequential prioritization up to projector $n$. Because the network may consist of multiple disconnected segments, this prioritization applies globally across all projectors.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 200,000$, $0 \le m \le 200,000$), representing the number of projectors and the number of thresholds, respectively.

Each of the subsequent $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that an interference threshold connects the projector indexed $u$ and the projector indexed $v$.

## Output
If it is impossible to find a viable cycle assignment, output `NO` on a single line.
If a viable assignment exists, output `YES` on the first line. On the second line, output $n$ space-separated integers (each being either 1 or 2) representing the pulse cycle assigned to each projector from 1 to $n$. This sequence must be the lexicographically smallest valid assignment.

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