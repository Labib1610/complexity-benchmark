# Problem A — Component Coating

Time limit: 2 s   Memory limit: 256 MB

An engineering project consists of $n$ structural components. Each component must be coated with exactly one type of protective film. The available film types are identified by the numbers 1, 2, and 3.

Certain pairs of components will be in direct physical contact in the final assembly. If two contacting components are coated with the same type of film, they will undergo a reaction that degrades the joint. Therefore, any two components that are in contact must be coated with different film types.

You need to determine if it is possible to assign a film type to every component safely. If multiple safe assignments exist, you must choose the one whose sequence of film types is lexicographically smallest (comparing the film type of component 1 first, then component 2, and so on).

## Input
The first line of the input contains two integers $n$ and $m$ — the number of components and the number of contact interactions ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that component $u$ and component $v$ are in direct contact.

## Output
If there is no way to assign the film types safely, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2, 3\}$), representing the film type applied to component $i$. The sequence must be the lexicographically smallest among all safe assignments.

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
