# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A major construction initiative demands the simultaneous deployment of **k** autonomous crews. The site coordinator has procured exactly **k** specialists, **k** heavy machinery units, and **k** dedicated operational shifts. Every resource in each of these three categories is identified by an integer from 1 to **k**.

Through rigorous safety testing, the coordinator has generated a catalog of **t** certified deployment configurations. A single configuration specifies one specialist, one machinery unit, and one shift that are certified to operate together safely. To ensure rapid processing, the sum of the three resource identifiers in any configuration never exceeds 66. Additionally, no specialist is ever part of more than 484 certified configurations in the catalog.

Your objective is to authorize exactly **k** configurations from the catalog such that every crew is fully equipped and no resources are double-booked. This means every specialist must be authorized exactly once, every machinery unit must be dispatched exactly once, and every shift must be utilized exactly once.

Determine whether it is possible to authorize a set of **k** configurations that meet these non-overlapping requirements, and if so, provide one such set.

## Input

The first line provides **k** and **t** (1 ≤ **k** ≤ 22, 0 ≤ **t** ≤ **k**·**k**·**k**), the number of required crews and the total number of configurations.
The subsequent **t** lines each contain three integers **x**, **y**, and **z** (1 ≤ **x**, **y**, **z** ≤ **k**), denoting a certified configuration comprising specialist **x**, machinery unit **y**, and shift **z**. All listed configurations are distinct.

## Output

If a valid authorization of **k** non-overlapping configurations exists, output `YES` on the first line. Following this, output **k** lines, each containing the three integers `x y z` of an authorized configuration. The configurations may be printed in any sequence. If multiple valid authorizations exist, any of them will be accepted.

If no such authorization is achievable, output `NO`.

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

In Example 2, both certified configurations require machinery unit 1, so it is impossible to authorize 2 configurations without reusing a machinery unit.
