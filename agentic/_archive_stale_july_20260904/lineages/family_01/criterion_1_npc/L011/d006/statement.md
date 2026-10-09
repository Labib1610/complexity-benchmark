# Problem A — Global Energy State

Time limit: 2 s   Memory limit: 256 MB

A physical model comprises $n$ distinct particles, indexed $1$ through $n$. You are required to calibrate the model by assigning each particle an energy state $c_i$ chosen from the set $\{1, 2, 3\}$.

Within this model, there are $m$ specific interacting pairs of particles. A complete calibration of the system $C = (c_1, c_2, \ldots, c_n)$ is deemed stable if and only if no two particles that form an interacting pair share the same energy state (i.e., $c_u \neq c_v$ for every interacting pair $u$ and $v$).

Your task is to find a stable calibration for all $n$ particles. If there are multiple valid ways to achieve stability, you must select the calibration $C$ that yields the strictly minimum possible value for the system's structural penalty $W(C)$. 

The penalty $W(C)$ is determined through the following sequential evaluation:
1. Start with an initial penalty $W = 0$.
2. For each particle index $i$ in increasing order from $1$ to $n$, update the penalty by multiplying the current $W$ by 4, and then adding the particle's energy state $c_i$.
The final value of $W$ after processing all $n$ particles is the penalty $W(C)$.

If it is impossible to find a stable calibration, report that no solution exists.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$), representing the number of particles and the number of interacting pairs, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that particle $u$ and particle $v$ form an interacting pair.

## Output
If no stable calibration can be formed, print a single line containing `NO`.
If a stable calibration is possible, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \ldots, c_n$, where $c_i \in \{1, 2, 3\}$ is the energy state assigned to particle $i$. If there are multiple stable calibrations, you must output the sequence that minimizes the structural penalty $W(C)$.

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