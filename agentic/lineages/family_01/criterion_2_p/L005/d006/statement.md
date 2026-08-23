# Problem B — Orbital Platform Balance

Time limit: 1 s   Memory limit: 256 MB

An orbital platform is constructed from $n$ storage modules, stabilized by a network of $m$ load-bearing struts. Each strut provides a physical link between a specific pair of modules.

Engineers must calibrate the harmonic frequency of the entire platform to prevent dangerous resonance. To achieve this, every individual module must be permanently assigned a frequency multiplier, which must be chosen as either 1 or 2.

A strut will remain stable and avoid buckling if and only if the product of the frequency multipliers of the two modules it links is exactly 2. 

Your task is to find a valid assignment of multipliers for all $n$ modules so that every strut in the network remains stable. If no such assignment exists under these constraints, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$) — the number of storage modules and the number of stabilizing struts.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that a strut links module $u$ and module $v$.

## Output
If it is impossible to stabilize the platform, print NO on a single line.
Otherwise, print YES on the first line. On the second line, print $n$ integers $p_1 \dots p_n$ (each in {1,2}), representing the lexicographically smallest valid sequence of frequency multipliers for modules $1$ through $n$.

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