# Problem B — Crew Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

A project must complete exactly **k** tasks, requiring the assembly of **k** distinct work crews. The available resources consist of **k** specialists, **k** machines, and **k** time slots. 

Each specialist is assigned exactly one specific machine for the duration of the project, and no two specialists are assigned to the same machine. A proposed crew assignment is a triplet containing one specialist, one machine, and one time slot. You are given a list of all feasible crew assignments. Every feasible assignment for a given specialist always pairs them with their uniquely assigned machine.

Your goal is to select exactly **k** assignments from this list. This selection must be arranged so that every specialist, every machine, and every time slot is utilized in exactly one crew. Determine if such a schedule can be constructed, and if possible, provide one valid selection.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of required crews and the number of feasible assignments.

Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a feasible assignment of specialist **x**, machine **y**, and time slot **z**. No assignment appears more than once in the list. For each specialist **x**, every listed assignment uses the same machine **y**, and different specialists are paired with different machines.

## Output

If a valid schedule of **k** crews exists, print `YES` on the first line. Then print **k** lines, each containing the three integers `x y z` of one chosen assignment (in any order). Any valid selection is accepted.

If no valid schedule exists, print `NO`.

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
