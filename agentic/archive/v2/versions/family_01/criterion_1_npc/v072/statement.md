# Operational Crew Allocation

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant operates using three distinct daily time slots, designated as 1, 2, and 3. There are $n$ workers indexed from 1 to $n$. Every worker must be assigned to work in exactly one time slot.

Due to shared tool sets and physical safety zones, certain pairs of workers are mutually restricted and cannot be scheduled in the same time slot. You are given a list of all such restricted worker pairs.

Your task is to determine whether a valid assignment of time slots exists such that no restricted pair of workers shares a time slot. If valid schedules exist, you must find the one that yields the lexicographically smallest sequence of assigned slots when listed in order of worker index (worker 1, worker 2, ..., worker $n$).

## Input
The first line of input contains two integers $n$ and $m$ — the number of workers and the number of restriction pairs.

- The headcount $n$ satisfies $1 \le n \le 40$.
- The restriction count $m$ is non-negative and cannot exceed the total number of distinct two-worker combinations that can be formed from $n$ individuals.

Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that worker $u$ and worker $v$ cannot be assigned to the same time slot. No restriction pair appears more than once in the input.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line.
On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the time slot assigned to worker $i$. If multiple valid assignments exist, print the one that is lexicographically smallest.

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
