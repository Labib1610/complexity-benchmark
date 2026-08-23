# Problem A — Rotation Roster

Time limit: 2 s   Memory limit: 256 MB

A facility operates continuously and requires technicians to be scheduled. Each technician must be assigned to exactly one daily rotation: morning (denoted by 1), afternoon (denoted by 2), or night (denoted by 3).

Certain pairs of technicians require the use of the same specialized calibration tool. Because there is only one such tool available per rotation, two technicians who share this requirement cannot be assigned to the same rotation.

You must determine a valid rotation assignment for every technician or report that no such roster is possible.

## Input
The first line contains two integers $n$ and $m$ — the number of technicians and the number of tool-sharing pairs. The facility guarantees at least one technician, but due to a strict locker limit, there are never more than forty technicians. The value $m$ ranges from zero up to the absolute maximum where every technician pairs with every other.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that technician $u$ and technician $v$ require the same tool.

## Output
If there is no way to assign the technicians to the rotations under these constraints, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ represents the rotation for technician $i$. If there are multiple valid rosters, you must output the one that assigns the lowest possible rotation number to technician 1. If ties remain, assign the lowest possible rotation number to technician 2, and so on.

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
