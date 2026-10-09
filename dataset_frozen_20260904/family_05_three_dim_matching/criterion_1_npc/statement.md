# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews. There are three groups, each with exactly **k** members:

- **k** specialists (group X), numbered 1..k,
- **k** machines (group Y), numbered 1..k,
- **k** time slots (group Z), numbered 1..k.

A crew consists of exactly one specialist, one machine, and one time slot. Only certain combinations work together; you are given a list of allowed combinations `(x, y, z)`.

Choose exactly **k** allowed combinations so that every specialist, every machine, and every time slot is used in **exactly one** chosen crew.

Determine whether this is possible, and if so report one valid set of crews.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen crew. Any selection in which every specialist, machine, and time slot is used exactly once is accepted; the crews may be printed in any order.

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

In Example 2, both allowed combinations use machine 1, so machine 2 can never be covered.
