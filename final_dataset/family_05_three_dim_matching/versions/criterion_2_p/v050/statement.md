# Problem B — Industrial Resource Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description

A major industrial project is planning its operations. The project requires scheduling exactly **k** distinct operational tasks. To execute a task, three resources must be allocated together:
- A specialist (identified by an ID from 1 to **k**)
- A piece of heavy machinery (identified by an ID from 1 to **k**)
- A deployment window (identified by an ID from 1 to **k**)

You are provided with a database of **t** feasible allocations. Each allocation is a record of three integers `(x, y, z)` indicating that specialist `x` can operate machinery `y` during deployment window `z`. 

Due to strict safety regulations, each specialist is certified to operate exactly one specific piece of machinery. Furthermore, the certifications are unique: no two specialists are certified for the same machinery. Consequently, in the provided database, every feasible allocation involving a particular specialist will always list the exact same machinery, and no machinery is associated with more than one specialist.

Your objective is to extract a valid operational schedule consisting of exactly **k** allocations from the database. For the schedule to be valid, it must utilize every specialist exactly once, deploy every piece of machinery exactly once, and occupy every deployment window exactly once. 

Determine if such a schedule can be formed. If so, provide the selected allocations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the required number of allocations and the total number of feasible records in the database.

This is followed by **t** lines, each containing three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing a single feasible allocation. No allocation is listed more than once. As dictated by the safety regulations, all records for a given specialist **x** will feature the same uniquely designated machinery **y**, and no two specialists share the same machinery.

## Output

If a valid schedule of **k** allocations can be formed, output `YES` on the first line. Following this, output **k** lines, each containing the three integers `x y z` of a chosen allocation. These lines may be printed in any order. If there are multiple valid schedules, any of them is acceptable.

If no such schedule is possible, output `NO`.

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
