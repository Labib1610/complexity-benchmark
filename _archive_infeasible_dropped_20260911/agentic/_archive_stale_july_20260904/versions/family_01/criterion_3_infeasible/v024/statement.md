# Problem C — Diagnostic Error Report

Time limit: 2 s   Memory limit: 256 MB

You are analyzing a network of $n$ interacting modules. Certain pairs of modules are known to be mutually incompatible. 

A subset of modules is defined as a "completely chaotic configuration" if every module in the subset is incompatible with every other module in the subset. A comprehensive system audit would require identifying the full spectrum of these configurations by evaluating all $2^n$ possible subsets of the $n$ modules. 

For your current diagnostic task, a full audit is not requested. You only need to isolate one completely chaotic configuration that contains exactly three modules. It is guaranteed that at least one such configuration exists within the network.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair of modules.
It is guaranteed that at least one completely chaotic configuration of size exactly 3 exists.

## Output
Print three integers $a$ $b$ $c$ on one line with $a < b < c$, representing the modules in the configuration. Output the lexicographically smallest such triple (smallest $a$; ties by smallest $b$; then smallest $c$).

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
