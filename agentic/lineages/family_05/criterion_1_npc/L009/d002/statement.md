# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility needs to launch a deployment plan involving three categories of assets:
- operators, identified by integers 1 through **k**,
- apparatuses, identified by integers 1 through **k**,
- shifts, identified by integers 1 through **k**.

A deployment unit consists of one operator, one apparatus, and one shift. You are provided with a catalog of allowed combinations `(x, y, z)`.

Two combinations are considered to interfere with each other if they share the same operator, they share the same apparatus, or they share the same shift. Your task is to select exactly **k** of the allowed combinations from the catalog such that no two selected combinations interfere with one another.

Determine whether such a non-interfering plan of size **k** can be formed, and if so, report one valid set of **k** combinations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing an allowed combination. No combination is listed more than once.

## Output

If a valid deployment plan of **k** non-interfering combinations exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen combination. Any valid plan is accepted; the combinations may be printed in any order.

If no valid plan exists, print `NO`.

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

In Example 2, both allowed combinations use apparatus 1. Thus, they interfere with each other and cannot be selected together. Since exactly 2 non-interfering combinations must be selected and only 2 combinations are available in total, it is impossible to form a valid plan.