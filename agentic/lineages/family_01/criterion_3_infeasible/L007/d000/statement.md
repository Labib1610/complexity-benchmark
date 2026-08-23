# Problem C — Fatal Configuration

Time limit: 2 s   Memory limit: 256 MB

A complex system contains $n$ modules. During stress testing, $m$ specific combinations of two modules were flagged as interfering with each other when operated simultaneously. 

The system administrator needs to isolate a fatal configuration. To do this, you must select exactly three distinct modules from the $n$ available. With up to 2000 modules, there are over a billion possible selections to evaluate. A selection of three modules is considered fatal if and only if every pair of modules within that selection interferes with each other according to the logs. 

You must search this space to find a fatal selection. It is guaranteed that the system is flawed and at least one such selection of three modules exists.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that module $u$ and module $v$ interfere with each other. 
It is guaranteed that at least one fatal selection of three modules exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that the pairs $\{a, b\}$, $\{a, c\}$, and $\{b, c\}$ are all listed as interfering in the input. 
If multiple fatal selections exist, output the one with the smallest value for $a$; if there is a tie, choose the one with the smallest value for $b$; and if still tied, the smallest value for $c$.

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
