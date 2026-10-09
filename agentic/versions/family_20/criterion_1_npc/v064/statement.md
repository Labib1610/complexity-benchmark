# Problem A — Prime-Time Dialogue Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description
A national broadcaster is producing a series of televised political dialogues. The production involves a specific set of politicians, each of whom has contractually agreed to participate in exactly three one-on-one dialogues.

The network has secured three distinct prime-time broadcast windows to air the entire series. Each dialogue must be assigned to exactly one of these three broadcast windows. To maximize viewership for each politician, no politician can have more than one of their dialogues aired in the same broadcast window. Because every politician is involved in exactly three dialogues, this means their appearances must be distributed such that one dialogue airs in the first window, one in the second, and one in the third.

You must determine if it is possible to assign every dialogue to a broadcast window under these conditions, and if so, provide a valid schedule.

## Input
The first line contains two integers **n** and **m** (n is even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of politicians and the total number of scheduled dialogues, respectively. Politicians are numbered from 1 to n.
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ n), indicating a dialogue between politician u and politician v.

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3}, representing the broadcast window assigned to each dialogue in the order they appear in the input. If multiple schedules are possible, any valid one will be accepted.
If no such schedule is possible, print `NO`.

## Example
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
YES
1 2 3 3 2 1
```
