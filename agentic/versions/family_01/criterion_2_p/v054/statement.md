# Problem B — Resonance Cascade Mitigation

Time limit: 1 s
Memory limit: 256 MB

The facility operates a high-energy particle accelerator containing $n$ magnetic confinement nodes. Due to the power infrastructure, the installation supports at least one node, and its maximum capacity is capped at 200,000 nodes. 

Each node requires a phase setting of either 1 or 2.

Electromagnetic leakage creates $m$ interference constraints. The total number of constraints may be zero, up to a hardware limit of 200,000. Whenever a constraint exists between a node at index $u$ and a node at index $v$, they must operate on different phase settings to prevent a resonance cascade.

You must find a valid phase assignment for all $n$ nodes. If multiple safe configurations exist, the initialization protocol requires the one where the sequence of phase settings (ordered from node 1 to $n$) is lexicographically smallest.

## Input
The first line provides the number of installed nodes $n$ and the number of detected constraints $m$.
The following $m$ lines each contain two integers $u$ and $v$, identifying the indices of the nodes involved in a constraint. These indices will always correspond to actual installed nodes (meaning they are between 1 and $n$, inclusive).

## Output
If it is impossible to stabilize the accelerator, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers (each either 1 or 2) representing the phase setting for each node, chosen to be the lexicographically smallest valid sequence.

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
