# Problem A — Artifact Exhibition

Time limit: 2 s   Memory limit: 256 MB

A museum curator is organizing an exhibition of $n$ historical artifacts. The museum has prepared three distinct display zones, identified by the numbers 1, 2, and 3. 

Certain pairs of artifacts share a conflicting historical context and cannot be placed in the same display zone. The curator must allocate each of the $n$ artifacts to exactly one of the three available zones so that no conflicting pair of artifacts shares a zone. (It is not strictly required to utilize all three zones; an allocation using fewer zones is perfectly valid as long as all conflicts are avoided). If no such allocation can be made, report that it is impossible.

## Input
The first line provides two integers $n$ and $m$ — the total number of artifacts and the number of conflicting pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a conflicting pair.

## Output
If no valid allocation exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $z_1, z_2, \dots, z_n$ (each in $\{1, 2, 3\}$), where $z_i$ is the display zone of artifact $i$. Any valid allocation is accepted.

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