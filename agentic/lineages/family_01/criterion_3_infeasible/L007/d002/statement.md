# Acoustic Resonance

Time limit: 2 s   Memory limit: 256 MB

An acoustic testing chamber contains $n$ tuning forks. During testing, $m$ specific pairs of forks were found to resonate destructively when struck together. 

The engineers need to identify a destructive triad to calibrate the dampening fields. A triad is defined by three distinct tuning forks $a$, $b$, and $c$ (with $a < b < c$) where $a$ and $b$ are recorded as resonating destructively, and $c$ is recorded as resonating destructively with both $a$ and $b$.

With up to 2000 tuning forks, there are many combinations to evaluate. It is guaranteed that at least one destructive triad is present in the test data. You must process the records to find it.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that fork $u$ and fork $v$ resonate destructively. 
It is guaranteed that at least one destructive triad exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ that form a destructive triad. 
If multiple destructive triads exist, output the one with the smallest value for $a$; if there is a tie, choose the one with the smallest value for $b$; and if still tied, the smallest value for $c$.

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