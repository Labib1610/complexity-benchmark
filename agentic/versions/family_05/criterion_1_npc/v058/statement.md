# Problem A — Synthesis Protocol

Time limit: 5 s   Memory limit: 256 MB

## Description

A research facility is documenting safe procedures for a new chemical process. The process involves three categories of resources: isotopes, solvents, and resonant frequencies. The facility has access to exactly **k** distinct isotopes (labeled 1 through **k**), **k** distinct solvents (labeled 1 through **k**), and **k** distinct frequencies (labeled 1 through **k**).

A single procedure requires the simultaneous combination of exactly one isotope, one solvent, and one frequency. The facility has identified a set of **t** such procedures that are confirmed to be safe and documented them in a registry.

When designing a comprehensive synthesis protocol, strict regulatory constraints must be met:
- A protocol is formed by selecting a collection of procedures from the registry.
- Across all selected procedures, no isotope may be utilized more than once.
- Similarly, no two selected procedures may share a solvent, nor may they share a frequency.
- No resource can be left idle; every individual isotope, every solvent, and every frequency must be incorporated into the protocol.

Your objective is to determine whether it is possible to formulate a comprehensive synthesis protocol that satisfies all these constraints, and if so, to list the specific procedures that comprise it.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the number of items in each resource category and the number of safe procedures in the registry.
Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), indicating a safe procedure that combines isotope **x**, solvent **y**, and frequency **z**. All listed procedures are unique.

## Output

If a valid comprehensive synthesis protocol can be formulated, print `YES` on the first line. Then, print **k** lines, each containing the three integers `x y z` of one procedure included in the protocol. If multiple valid protocols exist, any of them will be accepted; the procedures may be printed in any order.

If no such protocol can be formulated, print `NO`.

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

In Example 2, both safe procedures require solvent 1. Selecting both would violate the rule against reusing a solvent, but selecting only one would leave solvent 2 unused. Thus, no valid protocol is possible.
