# Relic Resonance Alignment

Time limit: 5 s
Memory limit: 256 MB

## Description
A museum is preparing an exhibit of $n$ relics in its Main Hall. The hall contains $n$ display cases arranged in a single straight line, numbered consecutively from 1 to $n$. Each relic must be placed in exactly one distinct display case.

To demonstrate the historical synergy between the items, $m$ pairs of relics are identified as having "resonance links". These links connect all the relics into a single, unified network that contains no closed loops. 

For every resonance link, an energy conduit is installed along the floor to connect the two respective display cases. The length of the conduit connecting a relic in display case $c_u$ and a relic in display case $c_v$ is exactly the absolute difference between their case numbers, $|c_u - c_v|$.

The museum has a maximum power draw of $B$ for all energy conduits combined, which corresponds directly to the total length of the conduits. Conduits may freely overlap along the hall, but the sum of the lengths of all conduits must not exceed $B$.

The curator guarantees that the provided resonance links satisfy two structural properties:
1. The $n$ relics can always be partitioned into two disjoint sets (one of which may be empty) such that every resonance link connects a relic from the first set to a relic from the second set.
2. The sum of the number of resonance links each relic is involved in is exactly $2m$.

Determine an assignment of the $n$ relics to the $n$ display cases such that the total length of all conduits is at most $B$, or state that the power requirements cannot be met.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$), indicating that relic $u$ and relic $v$ share a resonance link. (The links connect all relics with no closed loops, meaning $m = n - 1$).

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers — the display case numbers (a permutation of 1 to $n$) assigned to relics 1, 2, ..., $n$ respectively.
If the maximum power draw cannot be met, print `NO`.

## Example

**Input:**
```text
5 4 6
1 2
1 3
1 4
1 5
```

**Output:**
```text
YES
3 1 2 4 5
```
