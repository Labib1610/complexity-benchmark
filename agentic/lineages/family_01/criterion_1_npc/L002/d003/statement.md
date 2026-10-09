# Ternary Sequence Validation

Time limit: 2 s   Memory limit: 256 MB

You are developing a validation module for a new verification scheme. The scheme requires producing a valid ternary sequence $S$ of length $n$, where each element $S[i]$ is an integer chosen from the set $\{1, 2, 3\}$.

The sequence must satisfy a set of $m$ structural diversity constraints to ensure proper distribution of values. Each constraint specifies two 1-based indices $u$ and $v$. To satisfy the constraint, the sequence must have strictly different values at these two indices (i.e., $S[u] \neq S[v]$).

Your task is to determine whether there exists at least one valid sequence of length $n$ that satisfies all $m$ constraints simultaneously. The test suites include highly restrictive constraint sets designed to evaluate the efficiency of your validation logic, meaning naive left-to-right sequence generation may fail to complete within the time limit.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). 
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a diversity constraint between the elements at index $u$ and index $v$. 

## Output
If no such sequence can be constructed, output `NO` on a single line.
If a valid sequence exists, output `YES` on the first line. On the second line, output $n$ integers representing the valid sequence $S[1], S[2], \dots, S[n]$. If there are multiple valid sequences, any of them will be accepted.

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