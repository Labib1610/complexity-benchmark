# Problem A — Configuration Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A system must run exactly **k** operations. Each operation is defined by a configuration of three distinct parameters. For each parameter, the assigned value must be an integer from 1 to **k**.

Only certain configurations of the three parameters are stable; you are given a list of stable configurations `(p1, p2, p3)`.

Choose exactly **k** stable configurations so that, across your chosen operations, every value from 1 to **k** is used **exactly once** for the first parameter, **exactly once** for the second parameter, and **exactly once** for the third parameter.

Determine whether this is possible, and if so report one valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the value limit and the number of stable configurations.
Each of the next **t** lines contains three integers **p1**, **p2**, **p3** (1 ≤ p1, p2, p3 ≤ k), representing a stable configuration. No configuration is listed more than once.

## Output

If a valid selection of **k** configurations exists, print `YES` on the first line, then print **k** lines, each containing the three values `p1 p2 p3` of one chosen configuration. Any selection meeting the requirement is accepted; the configurations may be printed in any order.

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

In Example 2, both stable configurations use the value 1 for the second parameter, so the value 2 can never be covered for the second parameter.
