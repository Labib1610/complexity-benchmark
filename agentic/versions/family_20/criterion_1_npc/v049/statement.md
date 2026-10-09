# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A trunk grid is defined by a collection of splice points and the transmission cables that connect them. The topology of this grid strictly dictates that exactly three transmission cables meet at any given splice point.

Operations on the grid require assigning each transmission cable a state from the set {1, 2, 3}, representing distinct maintenance periods. A configuration of states is considered stable if and only if, at every single splice point, no two converging cables share the same state. Because there are exactly three cables at each point and three possible states, a stable configuration ensures that the cables at any junction all operate in completely different periods.

Your objective is to process the topology of a given trunk grid and establish whether a stable configuration of maintenance states is possible. If such a configuration can be achieved, you must output the state assignments for all cables.

## Input
The first line provides two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), which denote the total number of splice points and the total number of transmission cables, respectively.
The next $m$ lines each contain two integers $u$ and $v$ ($1 \le u < v \le n$), specifying that a single transmission cable links splice point $u$ and splice point $v$.

## Output
If a stable configuration is achievable, print `YES` on the first line. On the second line, print $m$ integers from the set {1, 2, 3}, indicating the state assigned to each cable, in the exact order the cables were listed in the input. If multiple valid configurations exist, any of them is acceptable.
If no stable configuration can be constructed, print `NO`.

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
