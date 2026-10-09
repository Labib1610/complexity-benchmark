# Problem A — Monitoring Coverage

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility of **n** sites and **m** links must be brought under monitoring. A sensor placed at a site observes that site and every site directly linked to it; a site is covered if it holds a sensor or is adjacent to one. With a budget of **k** sensors, decide whether every site can be covered, and if so report the placements. Link lengths and site functions are irrelevant; only adjacency matters. Because one sensor covers a whole neighbourhood, greedy placement often overlaps or leaves gaps, and finding a placement of only k that leaves nothing uncovered is the hard part.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 48, 0 ≤ m ≤ n·(n−1)/2, 0 ≤ k ≤ n).
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
