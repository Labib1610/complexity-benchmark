# Problem A — Fluid Routing Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A routing station directs fluid through a series of valves. The station supports a positive number of valves, up to a maximum of ninety. Each valve must be permanently set to either the open or closed position before operation begins. Intermediate positions are impossible.

Safety inspectors have documented a series of operational constraints. The number of constraints can be zero, and never exceeds four hundred. Each constraint specifies a fallback group of required valve positions. A constraint is satisfied if a minimum of one of its listed positions matches the actual state of the station's valves. If a constraint finds none of its listed positions matched, the station is deemed unsafe.

A position is denoted by the valve's identification number. A positive number means the valve must be open; a negative number means the valve must be closed. A single valve might be referenced by many constraints, potentially with conflicting required positions. The same valve may even be referenced multiple times within a single fallback group.

You must evaluate whether the entire station can be configured to satisfy all documented constraints concurrently. If possible, output a valid configuration.

## Input

The first line contains two integers $n$ and $m$, representing the actual count of valves and constraints, respectively. These values adhere strictly to the physical minimums and maximums detailed in the system overview.

The following $m$ lines each contain a sequence of non-zero signed integers $l_1, l_2, l_3$, representing the required positions in one fallback group. As expected, every referenced valve ID has a magnitude no greater than $n$.

## Output

If no comprehensive configuration exists, print a single line `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i$ is `1` if valve $i$ is open, and `0` if it is closed. Any configuration that satisfies all constraints is acceptable.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```
