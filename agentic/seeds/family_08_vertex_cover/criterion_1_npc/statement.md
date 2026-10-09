# Problem A — Guard Placement

Time limit: 5 s   Memory limit: 256 MB

## Description

A security office must watch every corridor of a building with **n** junctions and **m** corridors, each corridor joining two junctions. A guard posted at a junction watches exactly the corridors touching that junction, and a corridor counts as watched if a guard stands at either endpoint. Staffing allows a budget of **k** guards. Decide whether k guard posts can leave no corridor unwatched, and if so report the chosen junctions. Patrol routes and shift lengths are irrelevant; only which junctions a corridor touches matters. Covering each corridor in isolation is easy — the difficulty is a single set of k junctions touching all corridors at once.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 54, 0 ≤ m ≤ n·(n−1)/2, 0 ≤ k ≤ 18).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a corridor between junctions u and v. No corridor is listed twice.

## Output

If **k** guards can watch every corridor, print `YES` on the first line, then on the second line print the junction numbers where guards are placed, separated by spaces (at most k of them). Any placement of at most k guards that watches every corridor is accepted. If no corridors exist, the second line may be empty.

If it cannot be done with k guards, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 2
2 3
3 4
1 4
```

**Output**
```
YES
2 4
```

### Example 2

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
NO
```

### Example 3

**Input**
```
2 1 1
1 2
```

**Output**
```
YES
1
```

## Note

In Example 1, guards at junctions 2 and 4 touch all four corridors. In Example 2, a triangle needs at least two guards, so one is not enough.
