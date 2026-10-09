# Problem A — Crew Routing

Time limit: 5 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews. The resource network consists of three layers, each with a capacity of exactly **k** members:

- **k** specialists (layer X), numbered 1..k,
- **k** machines (layer Y), numbered 1..k,
- **k** time slots (layer Z), numbered 1..k.

A crew consists of exactly one specialist, one machine, and one time slot, forming a complete path through the layers. Only certain paths are viable; you are given a list of allowed combinations `(x, y, z)` representing a viable path from a specialist `x` to a machine `y` to a time slot `z`.

Your goal is to route exactly **k** non-overlapping paths through this network by choosing exactly **k** of the allowed combinations, so that every specialist, every machine, and every time slot is saturated (used in **exactly one** chosen path).

Determine whether this perfect saturation is possible, and if so report one valid set of paths.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the layer size and the number of allowed paths.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed path. No path is listed more than once.

## Output

If a valid selection of **k** paths exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen path. Any selection in which every specialist, machine, and time slot is used exactly once is accepted; the paths may be printed in any order.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

## Note

In Example 2, both allowed paths use machine 1, so machine 2 can never be saturated.
