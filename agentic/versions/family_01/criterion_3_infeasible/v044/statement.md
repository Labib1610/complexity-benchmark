# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

The facility operates on a strict two-shift system, but the current personnel roster is fundamentally flawed. To definitively prove to management that no valid assignment of workers to the two shifts can possibly exist, you must present an incontrovertible certificate of failure: a designated subset of workers such that every single pair of workers within this subset is mutually incompatible. 

Given $n$ workers, there are $2^n$ possible subsets to consider. Evaluating the provided incompatibility records to verify if all pairs within a subset are in conflict requires navigating a massive combinatorial space. You must develop a procedure that searches through these combinations to identify a valid certificate. The certificate you present must be a subset of exactly three workers. The roster data is guaranteed to contain at least one such subset.

Because multiple valid certificates may exist within the search space, you must report the lexicographically smallest one. A subset is lexicographically smaller than another if its smallest worker identifier is smaller; ties are resolved by comparing the second smallest identifiers, and then the third.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of workers and the number of known incompatibilities.
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that worker $u$ and worker $v$ are mutually incompatible.
It is guaranteed that at least one valid certificate of the required size exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$. These must be the identifiers of the workers in the lexicographically smallest valid certificate.

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
