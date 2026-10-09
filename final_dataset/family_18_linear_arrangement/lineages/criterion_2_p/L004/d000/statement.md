# Linear Module Alignment

Time limit: 5 s   Memory limit: 256 MB

## Description
An assembly facility requires placing $n$ distinct modules into $n$ consecutive slots along a straight rail. Each module must occupy exactly one slot, and the slots are numbered $1$ to $n$ in order.

The modules must be wired together using $m$ cables. Each cable directly links a specific pair of modules. The wiring specifications guarantee that $m = n - 1$ and that signals can be routed between any two modules via some sequence of cables. 

When module $u$ is installed in slot $P_u$ and module $v$ is installed in slot $P_v$, the physical length of the cable required to join them is exactly $|P_u - P_v|$. The total material cost is the sum of the lengths of all $m$ cables.

You are provided with a maximum budget $B$ for the total cable length. Determine whether it is possible to assign the $n$ modules to the $n$ slots such that the total cable length does not exceed $B$.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a cable must link module $u$ and module $v$. 
It is guaranteed that $m = n - 1$ and the cables integrate all $n$ modules into a single unified system.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers representing the slot numbers ($1$ to $n$, forming a permutation) assigned to modules $1, 2, \dots, n$ respectively. 
If no such assignment is possible, print `NO`.

## Example

### Input 1
4 3 4
1 2
2 3
2 4

### Output 1
YES
1 2 3 4

### Input 2
4 3 3
1 2
2 3
2 4

### Output 2
NO
