# Problem A — Fleet Routing and Promotions

Time limit: 2 s   Memory limit: 256 MB

## Description

A logistics company operates a fleet of $n$ delivery trucks. For the upcoming shift, the dispatcher must assign each truck to exactly one of two regional corridors: the "upper" corridor (denoted by 1) or the "lower" corridor (denoted by 0). A truck cannot be split between corridors, and no truck may remain unassigned.

To gather promotional material, the company has contracted $m$ freelance photographers. Each photographer submits a proposal containing exactly three potential photo opportunities. A photo opportunity consists of a specific truck traveling on a specific corridor. A photographer's contract is considered fulfilled if the final fleet routing allows them to capture **at least one** of their three proposed opportunities. If a photographer's proposal contains no opportunities that align with the actual routing, their contract fails. The same truck may be targeted by many photographers, sometimes on the upper corridor and sometimes on the lower.

You must determine whether there is a single, fleet-wide routing assignment that fulfills the contracts of **every** photographer simultaneously. If such a routing exists, you must report one valid assignment. 

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 90$, $0 \le m \le 400$).
Each of the next $m$ lines describes a photographer's proposal using three non-zero signed integers $l_1$, $l_2$, $l_3$, with $|l_i| \le n$. 
The absolute value $|l_i|$ represents the truck's ID. A positive integer indicates an opportunity where that truck is assigned to the upper corridor, while a negative integer indicates an opportunity where that truck is assigned to the lower corridor. 

## Output
If no routing assignment can fulfill all contracts, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$), where $s_i$ is the corridor assigned to truck $i$. If multiple valid assignments exist, any of them will be accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each photographer's proposal contains exactly three entries. It is possible for the same truck ID to appear more than once in a single proposal.
