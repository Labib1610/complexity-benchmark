# Problem B — Network Configurations

Time limit: 1 s
Memory limit: 256 MB

A communication grid consists of $n$ radio towers. You need to assign each tower $i$ a protocol flag $f_i$, which must be chosen from the set $\{1, 2\}$. 

There are $m$ critical links between specific pairs of towers. 

During operation, the network runs in synchronized time steps $t \ge 0$. Each tower maintains an active state from the set {Sync, Ping, Ack}. At time step $t=0$, every tower is initialized to the Sync state.
For each subsequent time step $t \ge 1$, a tower's state updates based on its assigned protocol flag:
- A tower with flag $f_i = 1$ follows the state transition cycle: Sync $\to$ Ping, Ping $\to$ Ack, Ack $\to$ Sync.
- A tower with flag $f_i = 2$ follows the state transition cycle: Sync $\to$ Ack, Ack $\to$ Ping, Ping $\to$ Sync.

To prevent interference, the two towers connected by any critical link must remain conflict-free. A critical link between tower $u$ and tower $v$ is conflict-free if and only if, at every time step $t \ge 1$:
- It is never the case that both towers are simultaneously in the Ping state.
- It is never the case that both towers are simultaneously in the Ack state.
(It is permissible for both towers to be in the Sync state at the same time).

Determine if a valid assignment of protocol flags exists for all towers such that all critical links are conflict-free. If no such assignment is possible, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of towers connected by a critical link.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $f_1 \dots f_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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