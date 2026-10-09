# Problem A — Festival Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

You are organizing a prestigious arts festival. The festival must be programmed with exactly **k** headline events.

You have received a list of **t** event proposals from various producers. Each proposal dictates three strict requirements: a specific performer, a specific venue, and a specific day of the festival. Each of these three requirements is represented by an integer from 1 to **k**.

To ensure a diverse and logistically sound festival, the final selection of **k** events must comply with the following scheduling rules:
- No two selected events may feature the same performer.
- No two selected events may be held at the same venue.
- No two selected events may take place on the same day.

Given the list of proposals, determine whether it is possible to choose exactly **k** events that satisfy all the rules. If such a schedule can be formed, provide one valid selection.

## Input

The first line provides two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the required number of events and the total number of proposals. 

Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), representing the performer, venue, and day for a single proposal. No proposal is duplicated in the input.

## Output

If a valid selection of **k** events exists, print `YES` on the first line. Then, print **k** lines, each containing the three parameters `x y z` of one of the chosen events. If there are multiple valid selections, you may output any of them. The events can be listed in any order.

If it is impossible to form a valid schedule, print `NO`.

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

In Example 2, both event proposals require venue 1. Selecting both would violate the scheduling rules, making it impossible to finalize 2 events.
