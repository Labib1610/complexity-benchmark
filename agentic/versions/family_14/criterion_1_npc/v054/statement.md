# Problem A — Survey Network

Time limit: 5 s   Memory limit: 256 MB

## Description

A topographic surveyor is mapping a region containing $n$ distinct landmarks, identified by integers from 1 to $n$. Within this region, there are $m$ potential bidirectional sightlines that can be cleared between specific pairs of landmarks. Each sightline has a known labor cost to clear.

Among the $n$ landmarks, a subset of $t$ landmarks are designated as primary triangulation pillars. The remaining landmarks are secondary points. Any landmark, whether primary or secondary, can serve as a junction to connect cleared sightlines.

The surveyor must ensure that all primary triangulation pillars are part of a single contiguous interconnected network. This means it must be possible to traverse between any two primary pillars using only the cleared sightlines. You must select a subset of the potential sightlines to clear such that this connectivity condition for the primary pillars is satisfied, while keeping the sum of the labor costs as low as possible. Determine this minimum total labor cost.

## Input

The first line contains three integers $n$, $m$, and $t$. 
Due to the standardized metric scales used on the surveyor's map:
- The number of primary pillars $t$ is at least 1 and at most the number of millimeters in one centimeter.
- The total number of landmarks $n$ is at least 1 and at most the number of centimeters in one meter.
- The number of potential sightlines $m$ is at least 0 and at most the maximum possible number of unique pairs of landmarks.

The second line contains $t$ distinct integers: the identifiers of the primary triangulation pillars.

Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$), representing a potential sightline between landmark $u$ and landmark $v$ that requires a labor cost of $w$. The labor cost $w$ is proportional to the physical distance and is an integer that is at least 1 and at most the number of millimeters in one kilometer.

It is guaranteed that clearing all available sightlines would be sufficient to interconnect all primary pillars.

## Output

Print a single integer: the minimum total labor cost required to interconnect all primary triangulation pillars.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, clearing sightlines through the secondary landmark 4 (labor cost 1+1+1 = 3) is cheaper than directly linking the three primary pillars (which would cost 2+2 = 4). In Example 3, there is only one primary pillar, so no sightlines need to be cleared.
