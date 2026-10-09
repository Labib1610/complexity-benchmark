# Problem B — Clockwork Assembly

Time limit: 1 s
Memory limit: 256 MB

A complex clockwork mechanism consists of $n$ gears, numbered 1 through $n$. Each gear must be configured into one of two directional modes, denoted by the integers 1 and 2. With $n$ gears, the complete configuration space spans $2^n$ potential global states. Identifying a viable global state requires navigating a strict set of mechanical dependencies.

You are provided with a blueprint detailing $m$ interacting pairs of gears. Whenever two gears form an interacting pair, their directional modes are mutually exclusive—they cannot be configured to the same mode. Your task is to evaluate the configuration space to determine if there exists at least one global state out of the $2^n$ possibilities that satisfies all $m$ mutual exclusion dependencies simultaneously.

Because the assembly tool requires deterministic input, if the search space contains multiple valid global states, you must output the one that is lexicographically smallest when written as a sequence of $n$ integers.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that gear $u$ and gear $v$ form an interacting pair.

## Output
If the configuration space contains no valid global state and the mechanism will jam, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid global state.

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
