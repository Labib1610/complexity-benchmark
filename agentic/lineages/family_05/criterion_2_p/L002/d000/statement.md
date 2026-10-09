# Problem B — Workflow Stage 2: Crew Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

A project requires a three-stage workflow to assemble **k** complete work crews. There are three groups of resources, each with exactly **k** members:

- **k** specialists (group X), numbered 1..k,
- **k** machines (group Y), numbered 1..k,
- **k** time slots (group Z), numbered 1..k.

A crew consists of exactly one specialist, one machine, and one time slot. You are given a list of allowed combinations `(x, y, z)`.

In **Stage 1** of the workflow, the human resources department evaluates the personnel and ensures that **each specialist is qualified on exactly one machine, and no two specialists share the same machine** — so the specialist-to-machine pairing is already fixed before you receive the data.

In **Stage 2**, which is your task, you must choose exactly **k** allowed combinations so that every specialist, every machine, and every time slot is used in **exactly one** chosen crew. Determine whether this is possible, and if so report one valid set of crews.

In **Stage 3**, the finance department will take your selected crews and allocate the budget for the assigned time slots. Your program only needs to handle Stage 2.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the group size and the number of allowed combinations forwarded from Stage 1.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. As guaranteed by Stage 1, for each specialist, every listed combination uses the same machine, and different specialists use different machines.

## Output

If a valid selection of **k** crews exists for Stage 2, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen crew (in any order). Any valid selection is accepted.

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

In Example 2, both specialists are restricted to time slot 1 by the allowed combinations. Because Stage 2 requires every time slot to be used exactly once, time slot 2 can never be covered, meaning the workflow cannot proceed to Stage 3.
