# Problem B — Orbital Platform Balance

Time limit: 1 s   Memory limit: 256 MB

An orbital platform consists of $n$ storage modules. The platform contains $m$ load-bearing struts, each connecting a specific pair of modules.

To maintain perfect structural balance, engineers must configure the internal pressure of each module. Every module must be permanently pressurized to one of two levels: 1 atm or 2 atm.

For a structural strut to properly bear the load without buckling, the sum of the pressures in the two modules it connects must be exactly 3 atm. 

You must determine a pressure level for all modules that ensures every strut safely bears its load. If the platform cannot be configured under these rules, indicate that it is impossible.

## Input
The first line provides $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), the number of modules and struts, respectively.
The following $m$ lines each contain two integers $u$ and $v$ — a pair of modules connected by a strut.

## Output
If the platform cannot be configured safely, output NO on a single line.
If it can, output YES on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (each in {1,2}), representing the lexicographically smallest valid sequence of pressure levels for modules $1$ through $n$.

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