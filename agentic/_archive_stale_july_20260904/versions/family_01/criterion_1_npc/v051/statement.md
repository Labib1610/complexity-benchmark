# Diplomatic Protocol

Time limit: 2 s   Memory limit: 256 MB

You are organizing an international summit attended by $n$ delegates, numbered 1 through $n$. The event relies on three concurrent discussion chambers, designated as Chamber 1, Chamber 2, and Chamber 3. Every delegate must be assigned to exactly one of these chambers.

Due to complex geopolitical tensions, there are $m$ documented historical grievances between specific pairs of delegates. Protocol dictates that two delegates who share a grievance cannot be placed in the same discussion chamber, as their presence together would derail the talks. A schedule is considered viable if absolutely no chamber contains a pair of delegates with a mutual grievance.

Your task is to determine whether a viable schedule exists. Because the organizers prefer to fill the chambers in order of their prestige (with Chamber 1 being the most prestigious), if there are multiple viable schedules, you must provide the one whose sequence of assignments is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ — the number of delegates and the number of historical grievances ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating a mutual grievance between delegate $u$ and delegate $v$.

## Output
If there is no viable schedule that satisfies all protocol constraints, output `NO` on a single line.
If a viable schedule exists, output `YES` on the first line. On the second line, output $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$), representing the chamber assignment for each delegate from 1 to $n$. If there are multiple viable schedules, output the lexicographically smallest sequence.

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
