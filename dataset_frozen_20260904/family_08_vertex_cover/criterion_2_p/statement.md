# Problem B — Guard Placement (Two Wings)

Time limit: 2 s   Memory limit: 256 MB

## Description

A building has **n** junctions (numbered 1..n) connected by **m** corridors. A guard stationed at a junction watches every corridor that touches it. A corridor is **watched** if a guard stands at at least one of its two endpoints.

The building splits into **two wings**, and **every corridor connects a junction in one wing to a junction in the other** — no corridor joins two junctions of the same wing. (The wings are not given to you; you may recover them from the corridors.)

You have a budget of **k** guards. Decide whether **k** guards can watch every corridor, and if so report where to place them.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 0 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a corridor. No corridor is listed twice, and the corridors follow the two-wing structure above.

## Output

If **k** guards can watch every corridor, print `YES` on the first line, then on the second line print the junction numbers where guards are placed (at most k of them), separated by spaces. Any placement of at most k guards watching every corridor is accepted. If no corridors exist, the second line may be empty.

If it cannot be done with k guards, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
4 4 1
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

### Example 3

**Input**
```
5 0 0
```

**Output**
```
YES

```

## Note

This is the same guard-placement problem as Problem A. The only difference is that the building has the two-wing structure (corridors run only between the two wings), which makes an efficient exact solution possible. In Example 1, guards at junctions 1 and 2 (one wing) watch all four corridors. In Example 2 no single guard can watch all four, so one is not enough.
