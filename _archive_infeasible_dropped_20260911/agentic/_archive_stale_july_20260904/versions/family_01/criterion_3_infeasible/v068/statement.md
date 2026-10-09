# Chamber Allocation Certificate

Time limit: 2 s
Memory limit: 256 MB

You are tasked with dividing $n$ experimental samples between two thermal chambers. However, certain pairs of samples are volatile when placed in the same chamber. It is already known that the provided list of $m$ volatile pairs makes a safe two-chamber division impossible.

Your objective is to provide a minimal counterexample to certify this impossibility. Specifically, you must identify three distinct samples that are mutually volatile with one another. Because all three cannot be separated into just two chambers, their presence alone guarantees the impossibility of the allocation.

To ensure the certification process is bounded, two structural guarantees are provided:
- The total number of volatile pair involvements, summed over all samples, does not exceed $400,000$.
- At least three samples in the dataset are guaranteed to each participate in two or more volatile pairs.

## Input

The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a volatile pair.
It is guaranteed that at least one mutually volatile triplet exists.

## Output

Print three integers $a$ $b$ $c$ on one line with $a < b < c$ such that all three pairs $a$–$b$, $a$–$c$, and $b$–$c$ are volatile. Output the lexicographically smallest such triplet (smallest $a$; ties by smallest $b$; then smallest $c$).

## Example 1
**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```
**Output:**
```
1 2 3
```

## Example 2
**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
**Output:**
```
1 2 4
```
