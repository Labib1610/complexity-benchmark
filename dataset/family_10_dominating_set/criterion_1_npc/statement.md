# Problem A — Monitoring Coverage

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility has **n** locations (numbered 1..n) connected by **m** direct links. If you install a sensor at a location, that sensor **monitors** its own location and every location directly linked to it.

A location is **covered** if it has a sensor or is directly linked to a location that has one. Using a budget of **k** sensors, decide whether every location can be covered, and if so report where to place the sensors.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 30, 0 ≤ m ≤ n·(n−1)/2, 0 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a direct link between locations u and v. No link is listed twice.

## Output

If **k** sensors can cover every location, print `YES` on the first line, then on the second line print the location numbers where sensors are placed, separated by spaces (at most k of them). Any placement of at most k sensors that covers every location is accepted.

If it cannot be done with k sensors, print `NO`.

## Examples

### Example 1

**Input**
```
5 4 1
1 2
1 3
1 4
1 5
```

**Output**
```
YES
1
```

### Example 2

**Input**
```
4 0 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 0 1
```

**Output**
```
YES
1
```

## Note

In Example 1, a sensor at location 1 monitors locations 1–5, so one sensor suffices. In Example 2 the four locations have no links, so each needs its own sensor and one is not enough.
