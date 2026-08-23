# Phase 2: Audit Contradiction Extraction

Time limit: 2 s   Memory limit: 256 MB

Our automated workforce compliance pipeline assigns staff to exactly two operational shifts. Phase 1 parses regulations to identify pairs of staff members who cannot work the same shift. 

Phase 1 has flagged that the current regulations make a two-shift assignment impossible. Your module (Phase 2) must extract a concrete contradiction to send to the Phase 3 reporting engine. To prove that two shifts are not enough, you must find a group of three distinct employees where each employee in the group is restricted from working with both of the other two.

The Phase 3 engine requires deterministic input. If multiple such groups of three exist, you must supply the one that is first when sorted by employee ID (i.e., minimizing the smallest ID, then the middle ID, then the largest ID).

## Input
The first line provides two integers $n$ and $m$, representing the total number of employees and the total number of logged restrictions, respectively. 
The facility requires at least $3$ employees to operate. The building is divided into $40$ identical zones, each with a strict safety limit of $50$ personnel, meaning the total workforce $n$ cannot exceed their combined maximum capacity. 
The number of restrictions $m$ is at least $3$. The auditing system limits the restriction log to exactly $2,000$ pages, where each page holds a maximum of $100$ records. Thus, $m$ is bounded by this total capacity or the maximum possible number of unique employee pairs, whichever is smaller.

Following this are $m$ lines, each containing two integers $u$ and $v$ representing a pair of employees who cannot share a shift.
It is guaranteed that at least one group of three mutually incompatible employees exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, representing the IDs of the three employees.
Output them in ascending order ($a < b < c$).
If there is a tie, output the group that minimizes $a$. If still tied, minimize $b$, and finally $c$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
