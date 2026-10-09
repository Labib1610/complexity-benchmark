# Problem B — Crew Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

A project must assemble exactly **k** complete work crews from a vast number of potential combinations. There are three distinct groups, each containing exactly **k** members:

- **k** specialists, numbered 1..k,
- **k** machines, numbered 1..k,
- **k** time slots, numbered 1..k.

A valid crew is defined as a triplet consisting of exactly one specialist, one machine, and one time slot. You are given a list of allowed crew combinations `(x, y, z)`.

Your objective is to explore the space of these allowed combinations and select exactly **k** of them such that every specialist, every machine, and every time slot is assigned to exactly one chosen crew. In this project, each specialist is qualified on exactly one machine, and no two specialists share the same machine.

Determine whether a valid selection of **k** crews exists among all possible configurations, and if so, report one valid set.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. For each specialist, every listed combination uses the same machine, and different specialists use different machines.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen crew (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
