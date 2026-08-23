# Line Station Scheduling

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates three distinct work channels (labeled 1, 2, and 3). There are $n$ technicians, indexed sequentially from 1 through $n$, who must each be assigned to exactly one channel.

The assignment proceeds under two primary requirements:
1. **Conflict Avoidance**: A list of $m$ pair restrictions specifies which pairs of technicians cannot be assigned to the same channel.
2. **Priority Minimization**: Channel 1 is preferred over channel 2, which is preferred over channel 3. When considering technicians in order from index 1 to $n$, earlier technicians take priority in receiving smaller channel numbers. Specifically, among all valid channel assignments, the chosen sequence $(s_1, s_2, \dots, s_n)$ must be lexicographically smallest.

Determine whether a valid channel assignment exists for all $n$ technicians. If so, determine the lexicographically smallest valid assignment sequence.

## Input
The first line contains two integers $n$ and $m$ — the number of technicians and the number of restriction pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that technician $u$ and technician $v$ cannot share the same channel.

## Output
If no valid assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ ($s_i \in \{1, 2, 3\}$), representing the assigned channel for each technician from 1 to $n$, yielding the lexicographically smallest valid sequence.

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
