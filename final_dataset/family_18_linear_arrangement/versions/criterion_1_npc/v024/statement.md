# Problem A — Agricultural Zone Assignment

Time limit: 5 s
Memory limit: 256 MB

## Description
A specialized agricultural facility is built as a single long greenhouse with $n$ consecutive climate zones, numbered $1$ to $n$. The facility will cultivate $n$ distinct crop varieties (numbered $1$ to $n$), with exactly one variety assigned to each zone.

Certain pairs of crops share a symbiotic watering system. There are $m$ such pairs. For each pair, a continuous irrigation pipe must be installed connecting their assigned zones. The length of a pipe is simply the difference between the zone numbers it connects (for instance, a pipe connecting a crop in zone 2 and a crop in zone 5 has a length of 3).

The total length of pipe used is the sum of the lengths of all $m$ individual pipes, which must not exceed the inventory of $B$ meters. Determine if there is an assignment of crops to zones such that the total length of all pipes is at most $B$.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that crop $u$ and crop $v$ require an irrigation pipe.

## Output
If the total pipe length can be kept within the budget, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer is the zone number (from $1$ to $n$) assigned to crop $i$. If no such assignment is possible, print `NO`.

## Example

### Input
```text
4 3 4
1 2
1 3
1 4
```

### Output
```text
YES
2 1 3 4
```
