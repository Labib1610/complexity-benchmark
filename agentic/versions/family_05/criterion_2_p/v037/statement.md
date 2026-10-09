# Problem B — Crew Assembly (Fixed Machines)

Time limit: 2 s   Memory limit: 256 MB

## Description

A project must assemble **k** complete work crews. There are three groups, each with exactly **k** members:

- **k** specialists (group X), sequentially numbered from one up to the group size,
- **k** machines (group Y), sequentially numbered from one up to the group size,
- **k** time slots (group Z), sequentially numbered from one up to the group size.

A crew consists of exactly one specialist, one machine, and one time slot. You are given a list of allowed combinations `(x, y, z)`.

In this project **each specialist is qualified on exactly one machine, and no two specialists share the same machine** — so the specialist-to-machine pairing is already fixed. The only thing left to decide is the time slots.

Choose exactly **k** allowed combinations so that every specialist, every machine, and every time slot is used in **exactly one** chosen crew. Determine whether this is possible, and if so report one valid set of crews.

## Input

The first line contains two integers **k** and **t**: the group size, which is at least one and capped by the maximum facility capacity of 1200, and the number of allowed combinations, which ranges from none up to the theoretical maximum where every specialist is available for every time slot.
Each of the next **t** lines contains three integers **x**, **y**, **z**, representing an allowed combination with positive identifiers not exceeding the group size. No combination is listed more than once. For each specialist, every listed combination uses the same machine, and different specialists use different machines.

## Output

If a valid selection of **k** crews exists, print `YES` on the first line, then print **k** lines, each containing the three members `x y z` of one chosen crew (in any order). Any valid selection is accepted.

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

This is the same crew-assembly (3-dimensional matching) problem as Problem A. The only difference is the promise that each specialist's machine is fixed and all distinct, which leaves only the time-slot choice and makes an efficient exact solution possible. In Example 2 both specialists' only allowed slot is 1, so time slot 2 can never be covered.
