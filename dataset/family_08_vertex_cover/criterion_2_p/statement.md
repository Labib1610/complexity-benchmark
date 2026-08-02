# Problem B — Two-Wing Guard Placement

Time limit: 2 s   Memory limit: 256 MB

## Description

A building has two wings. The **west wing** has **nA** junctions (numbered 1..nA) and the **east wing** has **nB** junctions (numbered 1..nB). Every corridor connects one west-wing junction to one east-wing junction — no corridor joins two junctions of the same wing.

A guard at a junction watches every corridor touching it. A corridor is watched if a guard stands at one of its two endpoints.

Find the **minimum** number of guards needed to watch every corridor.

## Input

The first line contains three integers **nA**, **nB**, and **m** (1 ≤ nA, nB ≤ 100000, 0 ≤ m ≤ 800000).
Each of the next **m** lines contains two integers **a** and **b** (1 ≤ a ≤ nA, 1 ≤ b ≤ nB): a corridor between west-wing junction a and east-wing junction b. No corridor is listed twice.

## Output

Print a single integer: the minimum number of guards needed to watch every corridor.

## Examples

### Example 1

**Input**
```
2 2 4
1 1
1 2
2 1
2 2
```

**Output**
```
2
```

### Example 2

**Input**
```
3 3 3
1 1
2 2
3 3
```

**Output**
```
3
```

### Example 3

**Input**
```
3 2 2
1 1
2 1
```

**Output**
```
1
```

## Note

In Example 3, both corridors touch east-wing junction 1, so a single guard placed there watches both.
