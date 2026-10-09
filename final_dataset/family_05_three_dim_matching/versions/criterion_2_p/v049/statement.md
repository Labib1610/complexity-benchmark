# Problem B — Extraction Schedule

Time limit: 2 s  
Memory limit: 256 MB  

## Description

During the qualification phase of a new extraction project, various operational tests were recorded. The tracking system monitors three categories of assets: exactly **k** operators, **k** rigs, and **k** zones. Every asset is identified by an integer from 1 to **k**.

Each recorded test is a triplet specifying the operator, the rig used, and the zone where the operation succeeded. These tests were conducted under strict hardware bindings. Before any testing began, each of the **k** operators was permanently assigned to a unique rig out of the **k** available rigs. An operator was physically restricted to their assigned rig, and no two operators were assigned the same rig. Consequently, in the recorded data, all entries for a specific operator will always feature the same rig, and no rig will ever appear in entries belonging to different operators.

The project is now transitioning to full deployment. For this phase, you must extract exactly **k** test records from the logs to serve as the final schedule. A schedule is only valid if every operator, every rig, and every zone is utilized in exactly one scheduled record. Determine whether it is possible to form a valid schedule from the recorded tests, and if so, output the selected records.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of assets in each category and the total number of recorded tests, respectively.

Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k). These integers denote the operator, rig, and zone of a single recorded test. No identical triplet is listed more than once. As guaranteed by the hardware bindings, any given operator **x** is paired with exactly one rig **y** across all their entries, and no two operators are paired with the same rig.

## Output

If a valid schedule of **k** records can be formed, print `YES` on the first line. Following this, print **k** lines, each containing the three integers `x y z` of a chosen record. The records may be printed in any order. If there are multiple valid schedules, any one of them will be accepted.

If no such schedule can be formed, print `NO`.

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
