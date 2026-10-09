# Problem A — Circuit Voltage Levels

Time limit: 2 s
Memory limit: 256 MB

An integrated circuit is being designed with $n$ logic components, labeled 1 through $n$. Your task is to assign each component a discrete operating voltage. The available voltage options for any component are 1, 2, and 3.

Certain pairs of components communicate via bidirectional data links. In order for communication to be successful across a link, the voltages assigned to the two connected components must form a permitted configuration. Specifically, the set of the two assigned voltages must be exactly one of the following:
- $\{1, 2\}$
- $\{1, 3\}$
- $\{2, 3\}$

You are provided with the number of components and the exact pairs that share a data link. You must output a fully functional voltage assignment for the circuit, or indicate if it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of logic components and the number of data links ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two distinct integers $u$ and $w$ ($1 \le u, w \le n$, $u \neq w$), representing a pair of components connected by a data link. It is guaranteed that each unordered pair of components appears at most once in the input.

## Output
If no valid voltage assignment can be found, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $a_1, a_2, \dots, a_n$ (where each $a_i \in \{1, 2, 3\}$), representing the voltage assigned to component $i$. Any valid assignment will be accepted.

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