# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility company manages a network of splice points connected by heavy-duty lines. The network design ensures a strict uniformity: if a technician stands at any splice point and counts the connecting lines, they will always find exactly three. 

Routine maintenance requires taking lines offline. This work is divided into exactly three distinct phases. Every line in the network must be assigned to exactly one of these phases. 

To prevent critical outages, a strict safety protocol applies to the splice points. During any single maintenance phase, a splice point can survive losing at most one of its connecting lines. Because there are only three phases available and every splice point is connected to exactly three lines, securing a splice point requires that all three of its lines are scheduled in completely different phases. The physical lengths of the lines and the crews assigned do not matter—the only requirement is that no two lines meeting at the same splice point are ever offline during the same phase.

Your task is to assign each line to one of the three maintenance phases such that the safety protocol is satisfied across the entire network. If no such global schedule is possible with only three phases, you must report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of splice points and the number of lines, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u < v \le n$), indicating that a line connects splice point $u$ and splice point $v$.

## Output
If a valid maintenance schedule exists, print `YES` on the first line. On the second line, print $m$ integers, each chosen from $\{1, 2, 3\}$, representing the phase assigned to each line in the order they were given in the input. If multiple valid schedules exist, any one is acceptable. If no valid schedule is possible, print `NO`.

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
