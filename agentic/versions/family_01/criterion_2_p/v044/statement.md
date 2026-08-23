# Optimal Workforce Configuration

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility must select an optimal workforce configuration from the space of possible daily schedules. The facility employs $n$ technicians, numbered 1 to $n$. A complete schedule assigns every single technician to a shift. The facility operates with exactly two shifts, labeled 1 and 2, meaning there are $2^n$ total configurations to consider.

A schedule is considered viable only if it satisfies a strict set of $m$ mutual exclusion constraints. Specifically, because of a shared specialized tool, certain pairs of technicians will cause a critical resource collision if assigned to the identical shift. A valid configuration must avoid all such collisions.

Your task is to evaluate the configuration space to find a viable schedule. In the event that multiple viable schedules exist, you must resolve the ambiguity by finding the one that minimizes the assignment sequence lexicographically (i.e., assigning lower-numbered technicians to shift 1 whenever possible). If the constraint system is over-constrained and no valid schedule exists in the entire space of $2^n$ possibilities, you must detect this and report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of technicians who are subject to a mutual exclusion constraint and thus cannot be assigned to the same shift.

## Output
If the search space contains no viable configuration, print a single line NO.
Otherwise print YES, followed by a second line containing $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$), representing the lexicographically smallest viable schedule.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
