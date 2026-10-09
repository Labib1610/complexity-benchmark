# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

At a project site, three distinct categories of resources are available: exactly **k** specialists, **k** heavy machines, and **k** scheduled time slots. The specialists are identified by integers from 1 to **k**. The machines and the time slots are similarly numbered from 1 to **k**.

Due to licensing and logistical constraints, not all resources can be combined. A planner has evaluated the safety requirements and compiled a comprehensive list of viable operational configurations. Each configuration in this list is given as a specific trio `(x, y, z)` consisting of one specialist, one machine, and one time slot that have been certified to operate together.

Your task is to select a subset of these certified configurations to form active work crews. To achieve a full deployment, you must choose exactly **k** configurations such that every single specialist is assigned, every single machine is utilized, and every single time slot is occupied exactly once across the chosen configurations. Determine if this full deployment is possible, and if so, report the configurations that make up the active crews.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the number of items in each resource category and the total number of certified configurations, respectively.
Each of the subsequent **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), describing a certified configuration. No configuration is repeated in the input.

## Output

If a full deployment is possible, output `YES` on the first line. Following that, output **k** lines, each containing the three integers `x y z` of a selected configuration. Any valid deployment meeting the criteria is acceptable, and the chosen configurations may be listed in any order.

If no such deployment is possible, output `NO`.

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

In Example 2, both certified configurations use machine 1, so machine 2 can never be utilized.
