# Render Contrast

Time limit: 1 s
Memory limit: 256 MB

A rendering system processes a composite scene consisting of $n$ distinct material layers, indexed from 1 to $n$. Every individual layer requires a specific transparency setting, which must be chosen as either the integer 1 or the integer 2.

To avoid rendering artifacts, the system is subject to $m$ interference restrictions. Every restriction links a specific pair of material layers. For a restriction to be successfully resolved, the bitwise XOR of the transparency settings chosen for the two linked layers must evaluate to exactly 3.

You need to establish whether a complete assignment of transparency settings exists for the $n$ layers such that all interference restrictions are resolved.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$). These represent a pair of layers that are bound by a single interference restriction.

## Output
If it is impossible to find a valid assignment of settings, output a single line with `NO`.
Otherwise, print `YES` on the first line. On the second line, provide $n$ integers denoting the lexicographically smallest valid sequence of transparency settings for layers 1 through $n$.

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