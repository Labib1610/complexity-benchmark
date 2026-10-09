# Problem A — Shift Allocation System

Time limit: 2 s
Memory limit: 256 MB

A manufacturing plant operates around the clock using exactly three daily shifts, designated as Shift 1, Shift 2, and Shift 3. The workforce comprises $n$ technicians. Every technician must be assigned to exactly one of these three shifts to ensure steady production.

Due to safety regulations regarding heavy machinery, specific pairs of technicians cannot be present on the factory floor during the same shift. The plant maintains a strict list of these restricted pairs. If two technicians are on this list, they must be assigned to different shifts.

The human resources software requires the final schedule to be entered as a numerical sequence, where the $i$-th number represents the shift assigned to technician $i$. To standardize data entry, the system automatically selects the valid sequence that is smallest when compared position by position from the first technician to the last (meaning the shift number for technician 1 is minimized first, then technician 2, and so on). You must determine if a valid shift assignment exists, and if so, output the sequence the system will select.

## Input
The first line provides two integers $n$ and $m$ — the total number of technicians and the number of restricted pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each contain two integers $u$ and $v$, identifying a pair of technicians who are restricted from sharing a shift.

## Output
If no valid assignment of shifts can satisfy the safety regulations, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print exactly $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the shift assigned to technician $i$. This sequence must be the one that is smallest when compared position by position from the first technician to the last.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
