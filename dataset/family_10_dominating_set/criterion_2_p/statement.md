# Problem B — Monitoring Coverage (Hierarchy)

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility of **n** sites and **m** links must be monitored; a sensor covers its own site and all directly linked sites, and a site is covered if it has a sensor or is adjacent to one. Here the links form a **hierarchy**: the sites are connected, contain no closed loops, and there are exactly n−1 links, so between any two sites there is a unique path. On such a loop-free structure the minimum number of sensors can be settled bottom-up without searching all placements. With a budget of **k** sensors, decide whether every site can be covered, and if so report the placements.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 200000, m = n − 1, 0 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a direct link. No link is listed twice, and the links form the connected, loop-free hierarchy described above.

## Output

If **k** sensors can cover every location, print `YES` on the first line, then on the second line print the location numbers where sensors are placed (at most k of them), separated by spaces. Any placement of at most k sensors covering every location is accepted.

If it cannot be done with k sensors, print `NO`.

## Examples

### Example 1

**Input**
```
5 4 1
2 1
3 1
4 1
5 1
```

**Output**
```
YES
1
```

### Example 2

**Input**
```
3 2 1
2 1
3 2
```

**Output**
```
YES
2
```

### Example 3

**Input**
```
4 3 1
2 1
3 1
4 3
```

**Output**
```
NO
```

## Note

This is the same monitoring-coverage problem as Problem A. The only difference is that the links form a loop-free hierarchy, which makes an efficient exact solution possible. In Example 1, a sensor at location 1 covers all five locations. In Example 3, no single location is linked to all others, so one sensor is not enough.
