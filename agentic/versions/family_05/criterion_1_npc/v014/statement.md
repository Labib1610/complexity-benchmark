# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A massive engineering project is putting together complete work crews. There are three separate rosters, each containing exactly the same number of members (the roster size, **k**):
- Specialists,
- Heavy machines,
- Operational time slots.

Members of each roster are uniquely identified by sequential integers starting from 1 up to the roster size.

To form a single valid crew, you must assign exactly one specialist to operate exactly one heavy machine during exactly one time slot. However, not all combinations are viable. You are provided with a catalog of certified protocols, where each protocol specifies a specialist, a machine, and a time slot that can safely operate together.

Your objective is to schedule exactly **k** crews using only the certified protocols such that no specialist, no machine, and no time slot is left unused. In other words, every single roster member across all three categories must be assigned to exactly one of the **k** chosen crews. Determine whether such a complete schedule is possible, and if so, report one valid set of crews.

## Input

The first line contains two integers: the roster size **k** and the number of certified protocols **t**.
The roster size **k** is a strictly positive integer. Because the site's armory holds exactly 22 safety harnesses and every scheduled specialist requires one, the roster size cannot exceed this inventory limit.
The tally of certified protocols **t** can be an empty list (0), or it can go up to the theoretical maximum where every possible combination of one specialist, one machine, and one time slot is listed.

Following this, there are **t** lines, each describing a single certified protocol via three integers **x**, **y**, and **z**. These values correspond to the IDs of the specialist, machine, and time slot respectively, meaning they start from the first member (1) and do not exceed the roster size **k**. No protocol is listed more than once.

## Output

If a complete schedule of **k** valid crews exists, output `YES` on the first line. Then, output **k** lines, each containing three integers `x y z` representing the specialist, machine, and time slot of a scheduled crew. Any selection in which every specialist, machine, and time slot is used exactly once is accepted; the crews may be printed in any order.

If no valid selection exists, output `NO`.

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

In Example 2, both certified protocols require heavy machine 1. Consequently, heavy machine 2 can never be assigned, making a complete schedule impossible.
