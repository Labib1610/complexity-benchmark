# Problem C — Crew Assembly: Certify Impossibility

Time limit: 1 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews from three groups of **k** members each — **k** specialists (group X), **k** machines (group Y), **k** time slots (group Z). A crew is one specialist, one machine, and one time slot, chosen from a list of allowed combinations `(x, y, z)`.

A valid plan uses every specialist, machine, and time slot exactly once. For every input in this problem it is **guaranteed that at least one specialist appears in no allowed combination at all** — that specialist can never be placed in a crew, so no valid plan can exist.

Report the smallest-numbered specialist that appears in no allowed combination.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1000, 0 ≤ t ≤ k·k): the group size and the number of allowed combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), an allowed combination. No combination is listed more than once. It is guaranteed that at least one specialist appears in no combination.

## Output

Print a single integer: the smallest-numbered specialist that appears in no allowed combination.

## Examples

### Example 1

**Input**
```
3 3
1 1 1
1 2 2
3 3 3
```

**Output**
```
2
```

### Example 2

**Input**
```
2 1
2 1 1
```

**Output**
```
1
```

## Note

In Example 1 specialist 2 appears in no allowed combination, so no plan can place them; 2 is the smallest such specialist. In Example 2 specialist 1 never appears.
