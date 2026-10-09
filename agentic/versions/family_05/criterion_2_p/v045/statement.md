# Problem B — Workflow Stage 2: Crew Assembly

Time limit: 2 s
Memory limit: 256 MB

## Description

Our manufacturing plant requires a three-step procedure to finalize work crews. A complete crew comprises one specialist, one machine, and one time slot. The plant has a specific group size *k*, meaning there are *k* specialists (identified by integers 1 through *k*), *k* machines (1 through *k*), and *k* time slots (1 through *k*).

The plant's physical capacity limits the group size *k* to a minimum of one and a maximum of twelve hundred.

In the first step of this procedure, human resources finalizes equipment certifications. They ensure every specialist is certified to operate exactly one machine, and that no two specialists are assigned to the same machine. This means the specialist-to-machine pairings are completely fixed.

In the second step, the planning department receives a list of *t* viable crew combinations. The number of viable combinations *t* can be as low as zero. At its upper limit, *t* reaches the theoretical maximum allowed by the certification rules (which occurs if every one of the *k* specialists is available during all *k* time slots). Each viable combination specifies a specialist, a machine, and a time slot. Because of the first step, any combination involving a particular specialist will always feature their uniquely assigned machine.

Your task is to execute this second step: select exactly *k* combinations from the viable list so that every specialist, every machine, and every time slot is deployed in exactly one crew.

(In the third step, finance allocates the payroll for the schedule you create. You only need to handle the second step.)

## Input

The first line provides two integers *k* and *t*: the group size and the number of viable combinations. The bounds for these values are defined by the plant's capacity and the certification rules described above.

The following *t* lines each provide three integers *x*, *y*, and *z* (between 1 and *k* inclusive), representing a viable combination of specialist *x*, machine *y*, and time slot *z*. No combination appears more than once in the input. Consistent with the first step's certification, all combinations involving a given specialist *x* will always specify the same machine *y*, and no two distinct specialists will be associated with the same machine.

## Output

If it is possible to form exactly *k* crews meeting all requirements, output `YES` on the first line. Then, output *k* lines, each containing the three members *x y z* of one chosen crew (in any order). Any valid selection is accepted.

If no valid selection exists, output `NO`.

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

In Example 2, both specialists are restricted to time slot 1 by the allowed combinations. Because the second step requires every time slot to be used exactly once, time slot 2 can never be covered, meaning the workflow cannot proceed to the third step.
