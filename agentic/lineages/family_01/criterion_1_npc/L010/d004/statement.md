# Problem A — Zero-Conflict Configuration

Time limit: 2 s
Memory limit: 256 MB

You are given a collection of $n$ items, indexed from 1 to $n$. You must assign each item a category from the set $\{1, 2, 3\}$. This assignment is represented as a sequence $g_1, g_2, \dots, g_n$, where $g_i \in \{1, 2, 3\}$ is the category assigned to item $i$.

You are also provided with a list of $m$ interacting pairs of items. 
For any complete configuration $g$, we define its *conflict score* as the total number of given interacting pairs $(u, v)$ for which $g_u = g_v$.

Your task is to determine if there exists a configuration with a conflict score of exactly 0. If such a configuration exists, you must output it.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$). This indicates that item $u$ and item $v$ form an interacting pair.

## Output
If no configuration has a conflict score of exactly 0, print a single line containing `NO`.
If at least one such configuration exists, output `YES` on the first line. On the second line, output the $n$ integers $g_1, g_2, \dots, g_n$ (each being 1, 2, or 3) representing the configuration.
In the event that more than one valid configuration has a conflict score of 0, you must output the one that is lexicographically smallest. That is, compare valid configurations by the category assigned to item 1, preferring the smaller category. If there is a tie, compare the category for item 2, and continue this sequential comparison up to item $n$ to break any remaining ties.

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