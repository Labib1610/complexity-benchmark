# Factory Roster Conflict Certification

Time limit: 2 s   Memory limit: 256 MB

In an industrial facility employing $n$ workers indexed from $1$ to $n$, specific pairs of workers are recorded as mutually incompatible, meaning they cannot share a shift. To establish proof of scheduling impossibility, auditors require a conflict certificate consisting of three distinct workers such that every pair among the three is recorded as mutually incompatible.

While evaluating all possible combinations of three workers involves examining up to $\binom{n}{3}$ candidate worker triplets, the facility audit protocol specifies that you must identify the single triplet $(a, b, c)$ with $1 \le a < b < c \le n$ where pairs $(a, b)$, $(a, c)$, and $(b, c)$ are all listed as incompatible. If multiple such triplets exist, you must select the lexicographically smallest one (minimizing $a$, then $b$, then $c$).

It is guaranteed that at least one mutually incompatible triplet exists in the input data.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), representing the total number of workers and the number of incompatible pairs, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that worker $u$ and worker $v$ are mutually incompatible. No unordered pair $(u, v)$ appears more than once.

## Output
Print three space-separated integers $a$, $b$, $c$ on a single line ($1 \le a < b < c \le n$) representing the lexicographically smallest worker triplet where all three constituent pairs are mutually incompatible.

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
