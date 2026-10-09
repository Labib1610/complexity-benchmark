# Problem B — Schedule Search

Time limit: 1 s
Memory limit: 256 MB

A factory manager is evaluating schedule sequences for $n$ employees. A complete schedule is a sequence of codes $s_1, s_2, \dots, s_n$. The manager has compiled a list of $m$ separation requirements. Each requirement identifies two employees who must receive different schedule codes.

You must search the space of possible schedule sequences to find one that satisfies all $m$ separation requirements. Because of operational limitations, the pool of allowed codes for any employee is restricted to exactly two values: 1 and 2. This means you are evaluating a space of $2^n$ possible sequences.

If there are multiple valid sequences that satisfy all requirements, you must resolve the tie by selecting the sequence that minimizes the codes. Specifically, a sequence $A$ is preferred over a different valid sequence $B$ if $A$ has a smaller code at the earliest employee index where $A$ and $B$ differ. If the search space contains no valid sequence, you must output NO.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of employees and the number of separation requirements.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), representing a separation requirement between employee $u$ and employee $v$.

## Output
If the search space contains no valid sequence, print a single line NO.
Otherwise, print YES on the first line. On the second line, print the $n$ integers $s_1, s_2, \dots, s_n$ (each either 1 or 2) representing the optimal valid schedule sequence.

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
