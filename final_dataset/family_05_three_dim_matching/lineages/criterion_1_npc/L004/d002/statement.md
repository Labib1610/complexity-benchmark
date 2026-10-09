# Problem A — Configuration Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A system must execute a schedule of exactly **k** operations. Each operation is defined by a configuration of three parameter positions: a primary setting, a secondary setting, and a tertiary setting. For each position, the assigned value must be an integer from 1 to **k**.

Only certain configurations of the three parameters are stable; you are given a list of **t** stable configurations `(p1, p2, p3)`.

You must select exactly **k** stable configurations to form your execution schedule. Your schedule is valid if and only if the collection of primary settings from your chosen configurations includes every integer from 1 to **k**. The same requirement applies independently to the collection of secondary settings, and to the collection of tertiary settings.

Determine whether a valid schedule can be formed, and if so, report one valid set of configurations.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 22, 0 ≤ **t** ≤ **k**³): the system scale and the number of stable configurations provided.

The next **t** lines each contain three integers **p1**, **p2**, **p3** (1 ≤ **p1**, **p2**, **p3** ≤ **k**), representing the primary, secondary, and tertiary values of a stable configuration. No configuration is listed more than once.

## Output

If a valid selection of exactly **k** configurations exists, print `YES` on the first line, then print exactly **k** lines, each containing the three values `p1 p2 p3` of one chosen configuration. Any selection meeting the requirement is accepted; the configurations may be printed in any order.

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

In Example 2, any schedule of 2 configurations would have to include both stable configurations. However, both configurations use the value 1 for their secondary setting. Consequently, the collection of secondary settings from the chosen configurations would be {1, 1}, which fails to include the integer 2 as required.