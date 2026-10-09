# Problem C — Structural Failure Extraction

Time limit: 2 s   Memory limit: 256 MB

Evaluating the structural integrity of a proposed organizational network requires analyzing the vast configuration space of all possible worker combinations. For a workforce of size $n$, there are $2^n$ potential groups that could be formed, and searching this expansive power set is often necessary to isolate critical structural flaws.

A group of workers is classified as "mutually hostile" if every single individual within that group has a documented friction with every other individual in the same group. 

Your task is to explore this configuration space to extract a certificate of network failure. To comply with the standardized reporting format, the extracted certificate must be a mutually hostile group that contains exactly three workers. The provided friction logs are guaranteed to contain at least one such group.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating a documented friction between this pair of workers.
It is guaranteed that at least one mutually hostile group of exactly three workers exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ such that all three pairs $a$-$b$, $a$-$c$, and $b$-$c$ have documented frictions. Output the lexicographically smallest such group (smallest $a$; ties by smallest $b$; then smallest $c$).

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
