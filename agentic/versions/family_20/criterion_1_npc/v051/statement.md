# Problem A — E-Sports Group Stage Scheduling

Time limit: 5 s
Memory limit: 256 MB

## Description
An e-sports league is organizing the group stage of its regional championship. The tournament features a series of 1-on-1 matches between participating players. The matchups have been drawn in advance, and the format guarantees that every participant is scheduled for exactly three matches.

The organizers need to distribute all the matches across exactly three play sessions. Multiple matches will happen concurrently during any given session. As a human being cannot be in two places at once, a participant can take part in at most one match per session. Because every player has three matches in total, they must therefore compete exactly once in each of the three sessions.

Determine whether it is possible to assign every match to one of the three sessions such that no player is scheduled to play more than once in the same session. If an arrangement is possible, output the schedule.

## Input
The first line contains two integers **n** and **m** (n is even, m = 3n/2, 2 ≤ n ≤ 2000), representing the number of participants and the total number of matches, respectively.
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u < v ≤ n), representing a match between participant **u** and participant **v**.

## Output
If a valid schedule exists, print `YES` on the first line. On the second line, print **m** integers from the set {1, 2, 3} representing the session assigned to each match, in the same order the matches were provided in the input. If no such schedule exists, print `NO`.

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
