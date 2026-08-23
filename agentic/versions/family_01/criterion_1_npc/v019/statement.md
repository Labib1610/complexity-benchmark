# Problem A — Synthetic Protein Tags

Time limit: 2 s   Memory limit: 256 MB

You are designing a synthetic protein chain consisting of $n$ distinct domains. Each domain must be modified with exactly one of three available chemical tags, which are identified by the integers 1, 2, and 3.

During the folding process, certain pairs of domains come into direct physical contact. You are given a list of $m$ such contact pairs. If two domains in a contact pair are modified with the identical chemical tag, they will bond incorrectly and cause the protein to misfold. Therefore, for every given contact pair, the two domains must be assigned strictly different tags.

Determine if there is a valid tag assignment for all $n$ domains that prevents misfolding. 

## Input
The first line contains two integers $n$ and $m$ — the number of domains and the number of contact pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a contact pair.

## Output
If no valid assignment exists, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $t_1, t_2, \dots, t_n$ (each in $\{1, 2, 3\}$), where $t_i$ is the tag of domain $i$. Among all valid assignments output the lexicographically smallest sequence (compare $t_1$ first, then $t_2$, and so on).

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
