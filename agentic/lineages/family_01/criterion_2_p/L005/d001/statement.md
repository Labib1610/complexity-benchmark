# Problem B — Molecular Assembly

Time limit: 1 s   Memory limit: 256 MB

A synthetic biology lab is designing a complex molecular structure using $n$ distinct protein building blocks. Each block must be folded into exactly one of two chiral states, designated as 1 and 2. There are $m$ structural interfaces between pairs of blocks. 

For the assembly to remain stable, any two blocks that share a structural interface must interlock, which requires them to be folded into different chiral states. Assign each building block exactly one chiral state such that if an interface exists between two blocks, they are placed in different states. If no such assignment can be made, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of blocks that share a structural interface.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), the lexicographically smallest valid assignment.

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