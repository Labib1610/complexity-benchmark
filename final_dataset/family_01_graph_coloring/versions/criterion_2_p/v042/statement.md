# Problem B — Reactive Cargo

Time limit: 1 s   Memory limit: 256 MB

A chemical facility manages $n$ volatile compounds and has exactly two available storage vaults, identified as 1 and 2. Because of chemical instability, certain pairs of these compounds will cause a dangerous reaction if stored in the same environment. There are $m$ such reactive pairs.

You must determine a safe storage plan that assigns every compound to one of the two vaults, ensuring that no two compounds from any reactive pair end up in the same vault. If no such configuration is possible, you must report it. 

## Input
The first line provides $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
The subsequent $m$ lines each contain two integers $u$ and $v$, representing a pair of compounds that react dangerously with one another.

## Output
If a safe storage plan is impossible, output a single line with the word NO.
If it is possible, output YES on the first line. On the next line, output $n$ integers $f_1 \dots f_n$ (where each $f_i \in \{1,2\}$), which represents the lexicographically smallest valid assignment of the $n$ compounds to the vaults.

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
