# Grand Corridor Curation

Time limit: 5 s
Memory limit: 256 MB

## Description
A museum is organizing an exhibition of $n$ artifacts. The exhibition will take place in the Grand Corridor, which features $n$ display pedestals arranged in a single straight line, numbered sequentially from 1 to $n$. Each artifact must be placed on exactly one distinct pedestal.

To guide visitors through the historical narrative, $m$ pairs of artifacts are designated as "narrative pairs". These narrative connections link all artifacts together into a single, unified structure containing no closed loops.

For every narrative pair, a distinct decorative runner is laid on the floor to connect their respective pedestals. The length of the runner connecting an artifact on pedestal $p_u$ and an artifact on pedestal $p_v$ is exactly the absolute difference between their pedestal numbers, $|p_u - p_v|$. 

The museum has a combined material budget of $B$ for all decorative runners. Runners may freely overlap along the corridor, but the total length of all runners used must not exceed $B$.

Find an assignment of the $n$ artifacts to the $n$ pedestals such that the sum of the lengths of all runners is at most $B$, or determine that the budget cannot be met.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$), indicating that artifact $u$ and artifact $v$ form a narrative pair. (The connections link all artifacts with no closed loops, meaning $m = n - 1$).

## Output
If a valid placement exists, print `YES` on the first line. On the second line, print $n$ integers — the pedestal numbers (a permutation of 1 to $n$) assigned to artifacts 1, 2, ..., $n$ respectively.
If the budget cannot be met, print `NO`.

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
