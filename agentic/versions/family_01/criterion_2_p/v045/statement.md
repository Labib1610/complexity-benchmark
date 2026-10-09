# Problem B — Alternating Cycles

Time limit: 1 s   Memory limit: 256 MB

A production facility utilizes $n$ automated manipulators. To balance the load, each manipulator must draw its energy from exactly one of two available generator networks, designated as network 1 and network 2. 

Because certain manipulators are installed in close proximity, their operational envelopes intersect. To ensure these intersecting manipulators do not strike each other, they must draw power from different generator networks, forcing them to move during alternating time windows.

You must determine an assignment of each manipulator to a generator network such that no two manipulators with intersecting envelopes share the same network. If no such configuration can be found, you must state so.

## Input
The first line provides the integers $n$ and $m$, representing the number of manipulators and the number of intersecting pairs.
The facility is built with a total power capacity of $400,000$ watts. Every installed manipulator consumes exactly $2$ watts. The number of manipulators $n$ is at least $1$ and at most the maximum number of manipulators this capacity can support. The number of intersecting pairs $m$ is at least $0$ and at most this exact same maximum limit.

Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating a pair of manipulators whose operational envelopes intersect.

## Output
If it is impossible to assign the networks without causing a collision risk, print a single line containing `NO`.
Otherwise, print `YES`, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$), representing the network assigned to each manipulator. If multiple valid configurations exist, output the one that is lexicographically smallest.

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
