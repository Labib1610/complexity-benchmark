# Problem B — Monitoring Coverage (Hierarchy)

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility has **n** locations (numbered 1..n) connected by **m** direct links. If you install a sensor at a location, that sensor **monitors** its own location and every location directly linked to it. A location is **covered** if it has a sensor or is directly linked to a location that has one.

In this facility the links form a **hierarchy**: the locations are connected, there are no closed loops of links, and there are exactly **n − 1** links in total (so between any two locations there is exactly one path).

Using a budget of **k** sensors, decide whether every location can be covered, and if so report where to place the sensors.

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
