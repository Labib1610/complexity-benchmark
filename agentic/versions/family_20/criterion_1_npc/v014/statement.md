# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A regional power authority maintains a network of distribution hubs. By design, the network is strictly uniform: every single hub acts as a convergence point for exactly three transmission lines.

To keep the network functional, all transmission lines must undergo scheduled maintenance. The authority has allocated exactly three distinct service shifts for this purpose. Whenever a transmission line is maintained, it is taken offline for the duration of its assigned shift.

To prevent any hub from becoming completely isolated from the grid, safety protocols dictate that no two lines connected to the same hub may be taken offline during the same shift. Because each hub connects exactly three lines and there are only three shifts available, this rule means that the three lines meeting at any given hub must each be assigned to a completely separate service shift.

Your task is to assign one of the three shifts (represented by the numbers 1, 2, and 3) to each transmission line such that the safety protocol is satisfied at every hub. If no such schedule is possible for the given network topology, you must report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$. The integer $n$ is the number of distribution hubs. It is guaranteed to be an even number, at least the minimum required to form a connection (a pair), and at most the maximum capacity of the monitoring system (two thousand). The integer $m$ represents the total number of transmission lines, which is exactly the amount required for every hub to connect to exactly three lines.

Each of the next $m$ lines provides two integers $u$ and $v$, specifying a transmission line between the hub labeled $u$ and the hub labeled $v$. Hub labels are positive integers up to $n$, and $u$ will always be strictly less than $v$.

## Output
If a valid maintenance schedule can be formed, print `YES` on the first line. On the second line, print $m$ integers chosen from {1, 2, 3} — the shift assigned to each transmission line in the order they appear in the input (lines sharing a hub must receive different shifts). Otherwise, print `NO`.

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
