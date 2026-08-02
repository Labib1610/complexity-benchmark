# Problem C — Unreachable Location

Time limit: 1 s   Memory limit: 256 MB

## Description

A facility has **n** locations (numbered 1..n) connected by **m** direct links. A sensor installed at a location monitors its own location and every location directly linked to it. A location is **covered** if it has a sensor or is directly linked to one.

In this facility the budget is **k = 0**, so no sensors can be installed. The facility also contains at least one location with **no links at all** — such a location has no sensor and no linked neighbor that could carry one, so it can never be covered.

Report the smallest index of a location that has no links.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 200000, 0 ≤ m ≤ 200000, k = 0).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a direct link. No link is listed twice. It is guaranteed that at least one location has no links.

## Output

Print a single integer: the smallest index of a location that has no links.

## Examples

### Example 1

**Input**
```
4 1 0
1 2
```

**Output**
```
3
```

### Example 2

**Input**
```
3 0 0
```

**Output**
```
1
```

## Note

In Example 1, locations 3 and 4 have no links; the smallest such location is 3.
