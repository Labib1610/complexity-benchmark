# Problem A — Surgical Schedule

Time limit: 5 s   Memory limit: 256 MB

## Description

A hospital administrator must schedule exactly **k** critical surgeries. There are three resource pools, each with exactly **k** available instances:

- **k** surgeons (group X), numbered 1..k,
- **k** operating rooms (group Y), numbered 1..k,
- **k** time blocks (group Z), numbered 1..k.

A procedure requires exactly one surgeon, one operating room, and one time block. Only certain combinations are viable based on surgeon availability and room equipment; you are given a list of allowed combinations `(x, y, z)`.

Choose exactly **k** allowed combinations so that every surgeon operates exactly once, every operating room is used exactly once, and every time block is allocated exactly once.

Determine whether this full schedule is possible, and if so report one valid set of procedures.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the resource pool size and the number of viable combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), a viable combination. No combination is listed more than once.

## Output

If a valid selection of **k** procedures exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one scheduled procedure. Any schedule in which every surgeon, operating room, and time block is used exactly once is accepted; the procedures may be printed in any order.

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

In Example 2, both viable combinations use operating room 1, so operating room 2 can never be covered.
