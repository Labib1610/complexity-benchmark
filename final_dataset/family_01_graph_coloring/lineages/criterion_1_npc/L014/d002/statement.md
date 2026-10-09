# Problem A — Circuit Voltage Levels

Time limit: 2 s
Memory limit: 256 MB

You are configuring a custom integrated circuit consisting of $n$ logic components, numbered 1 through $n$. Each component must be supplied with a discrete operating voltage level of 1, 2, or 3.

The circuit contains data links between certain pairs of components. For a data link to function correctly, there must be a non-zero potential difference between the two components it connects. Therefore, the two components sharing a link cannot be supplied with the identical voltage level. 

Note that the test data includes configurations specifically structured such that evaluation approaches which process components in numerical order, or sort them solely by their number of connections, will explore too many invalid states.

You are given the total number of components and the specific pairs that are connected by data links. Determine a valid voltage assignment for all $n$ components that ensures every data link is functional, or report that no such assignment exists.

## Input
The first line contains two integers $n$ and $m$ — the number of logic components and the number of data links ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two distinct integers $u$ and $w$ ($1 \le u, w \le n$, $u \neq w$), representing a pair of components connected by a data link. It is guaranteed that each unordered pair of components appears at most once in the input.

## Output
If no valid voltage assignment can be found, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $a_1, a_2, \dots, a_n$ (where each $a_i \in \{1, 2, 3\}$), representing the voltage level assigned to component $i$. Any valid assignment will be accepted.

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