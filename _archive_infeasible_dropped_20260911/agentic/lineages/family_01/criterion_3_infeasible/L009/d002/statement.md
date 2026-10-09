# Problem C — Tripartite Feedback Loop

Time limit: 2 s
Memory limit: 256 MB

An experimental fusion reactor is equipped with $n$ plasma modules, numbered $1$ to $n$. During calibration, engineers tested pairs of modules and recorded $m$ specific pairs that can synchronize their frequencies perfectly.

To initiate the main fusion sequence, the reactor’s control system must isolate a "tripartite feedback loop." This requires selecting exactly three distinct modules that are completely mutually synchronized. In other words, within this chosen group of three, every module must have a confirmed frequency synchronization with both of the other two modules.

Theoretical safety checks ensure that the provided calibration logs always contain at least one valid tripartite feedback loop. Your task is to pinpoint the modules that form it.

## Input
The first line consists of two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, signifying that module $u$ and module $v$ can synchronize their frequencies. These synchronizations are symmetric (the order of $u$ and $v$ does not matter), and no pair is listed more than once.
It is guaranteed that at least one valid tripartite feedback loop exists.

## Output
Print three integers $x$, $y$, and $z$ on a single line, separated by spaces, such that $x < y < z$. These are the identifying numbers of the three modules in your chosen feedback loop. If there is more than one valid group of three, you must select the one that minimizes the value of $x$. If multiple groups share the same $x$, minimize $y$; if ties still persist, minimize $z$.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```