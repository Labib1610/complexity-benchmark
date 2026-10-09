# Problem A — Surgery Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

A hospital must schedule **k** complex surgeries. There are three resource pools, each containing exactly **k** distinct elements:

- **k** lead surgeons, numbered 1..k,
- **k** operating theaters, numbered 1..k,
- **k** patient cases, numbered 1..k.

A scheduled surgery requires exactly one surgeon, one theater, and one patient case. Because of medical specialties and equipment needs, only certain specific combinations of surgeon, theater, and patient case are medically viable; you are given a list of these viable combinations `(x, y, z)`.

You must select exactly **k** viable combinations to ensure every lead surgeon operates exactly once, every operating theater is utilized exactly once, and every patient case is treated exactly once.

Determine whether this is possible, and if so report one valid set of scheduled surgeries.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the resource pool size and the number of viable combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable combination of a surgeon, theater, and patient case. No combination is listed more than once.

## Output

If a valid selection of **k** surgeries exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one scheduled surgery. Any selection in which every surgeon, theater, and patient case is used exactly once is accepted; the scheduled surgeries may be printed in any order.

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

In Example 2, both viable combinations require operating theater 1, so operating theater 2 can never be utilized.
