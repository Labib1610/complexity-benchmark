# Assembly Sequencing

Time limit: 2 s   Memory limit: 256 MB

You are configuring the production schedule for a high-precision manufacturing plant. The daily production cycle is divided into exactly three sequential operational blocks (labeled 1, 2, and 3, in chronological order). 

There are $n$ distinct manufacturing tasks that must be executed. You must assign each task to exactly one of the three operational blocks. 

You are given a list of $m$ resource conflicts. Each conflict indicates that two specific tasks require the same critical robotic arm. Because a robotic arm lacks the capacity to process tasks concurrently, any two tasks that share an arm must be temporally separated. Specifically, for every given pair of tasks that share an arm, one task in the pair must be assigned to a strictly earlier operational block than the other.

Your objective is to determine if all $n$ tasks can be scheduled into the three operational blocks without violating any resource conflicts. If a valid schedule exists, output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$) — the number of manufacturing tasks and the number of resource conflicts.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a pair of tasks that share a robotic arm.

## Output
If there is no valid way to schedule the tasks, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (each in {1, 2, 3}), where $b_i$ is the operational block assigned to task $i$. If there are multiple valid schedules, any valid schedule is accepted.

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