# Problem B — Resource Scheduling

Time limit: 2 s
Memory limit: 256 MB

## Description

An industrial project needs to finalize exactly **k** extraction teams. The available resources consist of three categories:

- **k** operators, identified by integers from 1 up to **k**,
- **k** drilling rigs, identified by integers from 1 up to **k**,
- **k** daily shifts, identified by integers from 1 up to **k**.

An extraction team is formed by assigning exactly one operator, one drilling rig, and one daily shift. You are provided with a list of safety-approved configurations `(x, y, z)`.

Due to strict licensing restrictions, each operator is exclusively licensed to operate exactly one specific drilling rig, and no two operators are licensed for the same rig. Consequently, the operator-to-rig associations are inherently fixed. The only remaining decision is the assignment of shifts.

Your task is to select exactly **k** approved configurations such that every operator, every drilling rig, and every shift is scheduled in **exactly one** chosen team. Determine whether such a schedule is possible, and if so, report one valid set of teams.

## Input

The first line contains two integers **k** and **t**: the required number of teams and the number of approved configurations. The value of **k** is at least 1, and is limited by a maximum capacity equal to the number of months in exactly one century. The value of **t** is at least 0, and will not exceed the total possible number of distinct operator-and-shift pairs.

Each of the next **t** lines contains three valid identifiers **x**, **y**, **z**, representing an approved configuration. No configuration is listed more than once. Consistent with the licensing restrictions, for any given operator, every listed configuration will specify the same drilling rig, and different operators will always be associated with different drilling rigs.

## Output

If a valid selection of **k** teams exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen team (in any order). Any valid selection is accepted.

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
