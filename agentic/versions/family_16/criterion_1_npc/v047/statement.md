# Problem A — Bureaucratic Bottleneck

Time limit: 5 s
Memory limit: 256 MB

## Description

The Grand Council consists of $m$ distinct Magistrates who must process $j$ pending petitions.

Each petition must navigate a rigid bureaucratic procedure, which is defined as a sequence of hearings. Each hearing mandates the undivided attention of a specific Magistrate for a predetermined number of hours.

The procedures are governed by the following mandates:
- The hearings for a given petition must be executed in the exact sequence specified. A hearing for a petition may only commence after the preceding hearing for that same petition has completely concluded.
- A Magistrate may only preside over one hearing at any given time.
- Once a hearing is initiated, the Magistrate must work on it continuously until it is finished; interruptions are strictly forbidden.
- **Guarantee 1:** The total cumulative duration of all hearings across all petitions is at most 50,000 hours.
- **Guarantee 2:** No single petition will require more than 50 hearings.

Determine the scheduling of all hearings that minimizes the hour at which the final hearing concludes. Output this earliest possible completion hour.

## Input

The first line contains two integers $j$ and $m$ ($1 \le j \le 10$, $1 \le m \le 10$).
Each of the subsequent $j$ lines details a single petition. Each line starts with an integer $o$ (the number of hearings for this petition), followed by $o$ pairs of integers. Each pair consists of a `magistrate` index ($1 \le magistrate \le m$) and the required `hours` ($1 \le hours \le 1000$), representing the hearings in their required order.
The total number of hearings across all petitions combined will not exceed 50.

## Output

Print a single integer: the earliest possible hour when all petitions are completely processed.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical petitions each pass through Magistrates 1, 2, and 3 (2 hours each); the second petition trails the first through the process and finishes at hour 8. In Example 3, the two petitions require different Magistrates and are processed in parallel, finishing at hour 4.
