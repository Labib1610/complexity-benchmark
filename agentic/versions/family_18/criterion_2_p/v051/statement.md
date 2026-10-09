# Problem B — Archival Arrangement

Time limit: 5 s   Memory limit: 256 MB

## Description
A museum is exhibiting $n$ historical manuscripts, uniquely numbered from 1 to $n$. The exhibition hall consists of a single long gallery with $n$ display pedestals arranged in a straight line, numbered sequentially from 1 to $n$. Each manuscript must be placed on exactly one pedestal.

Certain pairs of manuscripts share a direct thematic link. Visitors studying a linked pair must walk between their pedestals. If one manuscript is on pedestal $x$ and the other is on pedestal $y$, the walking distance is exactly $|x - y|$ meters. The museum curators have established a strict upper limit of $B$ meters for the sum of the walking distances across all directly linked pairs combined.

The thematic links tie the exhibition into a single cohesive collection: it is possible to trace a conceptual path from any manuscript to any other through a sequence of these direct links. To keep the exhibition focused, the curators have selected the absolute minimum number of direct links required to ensure every manuscript is part of this unified whole.

Determine a valid placement of the $n$ manuscripts onto the $n$ pedestals such that the total walking distance does not exceed $B$.

## Input
The first line contains three integers $n$, $m$, and $B$.  
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that manuscript $u$ and manuscript $v$ share a direct thematic link. (The minimal linking property guarantees that $m = n - 1$).

## Output
If the distance limit can be satisfied, print `YES` on the first line. On the second line, print $n$ integers representing the pedestal assignments for manuscripts 1 through $n$, respectively. The assignments must be a permutation of the integers from 1 to $n$.  
If it is impossible to satisfy the limit, print `NO`.

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
