# Problem A — Crew Assembly

Time limit: 5 s   Memory limit: 256 MB

## Description

A corporate initiative requires the deployment of **k** distinct task forces. Each task force must be assigned exactly one expert, one apparatus, and one shift. 

The company employs experts, owns apparatuses, and operates shifts. Experts, apparatuses, and shifts are each assigned sequential ID numbers starting from 1 up to the required number of task forces.

Only certain specific groupings of an expert, an apparatus, and a shift are certified to operate together without failure. You are provided a log of these certified groupings.

Your objective is to deploy exactly **k** task forces using only certified groupings. To ensure full coverage and prevent scheduling conflicts, no two deployed task forces may feature the same expert, the same apparatus, or the same shift. 

Determine if a full deployment is achievable, and if so, output one such arrangement.

## Input

The first line provides two integers **k** and **t**. The initiative must deploy at least one task force. The company fleet consists of 22 transport vans, and since each task force requires its own van, this sets the absolute upper limit for **k**. The value **t** represents the number of certified groupings available in the log. This can be as low as zero, or as high as the scenario where every expert is certified with every apparatus on every shift.

Following this are **t** lines, each containing three integers **x**, **y**, and **z**. These represent a certified grouping consisting of expert **x**, apparatus **y**, and shift **z**. The log contains no duplicate groupings.

## Output

If it is possible to form exactly **k** task forces under the given restrictions, output `YES` on the first line. Then, output **k** lines, each containing the three integers `x y z` representing the expert, apparatus, and shift of a deployed task force. The groupings may be listed in any order.

If it is impossible to meet the requirements, output `NO`.

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

In Example 2, both certified groupings use apparatus 1. Since deployed task forces cannot share an apparatus, at most one grouping can be selected, making it impossible to assemble 2 task forces.
