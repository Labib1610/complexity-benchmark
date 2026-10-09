# Problem B — Crew Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews. There are three groups, each with exactly **k** members:

- **k** specialists (group X), numbered 1..k,
- **k** machines (group Y), numbered 1..k,
- **k** time slots (group Z), numbered 1..k.

A crew consists of exactly one specialist, one machine, and one time slot. You are given a list of allowed combinations `(x, y, z)`.

In this project, the allowed combinations follow strict rules: if any two combinations list the same specialist, they are guaranteed to list the same machine. Similarly, if any two combinations list the same machine, they are guaranteed to list the same specialist.

Choose exactly **k** allowed combinations so that every specialist, every machine, and every time slot is used in **exactly one** chosen crew. Determine whether this is possible, and if so report one valid set of crews.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. The combinations are guaranteed to follow the rule that the same specialist never appears with two different machines, and the same machine never appears with two different specialists.

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

## Note

In Example 2 both specialists' only allowed slot is 1, so time slot 2 can never be covered.
