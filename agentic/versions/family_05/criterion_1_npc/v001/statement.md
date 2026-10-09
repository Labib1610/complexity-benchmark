# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews. The project has exactly **k** members in each of the following categories:

- **k** specialists, numbered 1..k,
- **k** machines, numbered 1..k,
- **k** time slots, numbered 1..k.

A crew requires a specialist, a machine, and a time slot. Only certain setups work together; you are given a list of compatible setups `(x, y, z)`.

Choose exactly **k** compatible setups so that every specialist, every machine, and every time slot is assigned to **exactly one** chosen crew.

Determine whether this is possible, and if so report one valid set of crews.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the category size and the number of compatible setups.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a compatible setup. No setup is listed more than once.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line, then print **k** lines, each containing the members `x y z` of one chosen crew. Any selection in which every specialist, machine, and time slot is used exactly once is accepted; the crews may be printed in any order.

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

In Example 2, both compatible setups use machine 1, so machine 2 can never be assigned.
