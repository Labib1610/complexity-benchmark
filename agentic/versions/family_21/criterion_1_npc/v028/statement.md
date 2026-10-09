# Problem A — Corporate Restructuring

Time limit: 5 s   Memory limit: 256 MB

## Description
A sprawling conglomerate is reorganizing its $n$ departments. Currently, the departments interact via $m$ joint initiatives. Each initiative connects exactly two departments, allows bidirectional communication, and carries a specific cancellation penalty (representing the cost of breaking contracts).

Among the departments, $k$ have been identified as the power bases of rival executives. The CEO has mandated that these $k$ power bases must be entirely segregated. You must cancel a selection of joint initiatives such that no sequence of active initiatives connects any two different power bases. Departments that are not power bases may end up connected to at most one power base, or none at all—their exact placement does not matter, as long as the power bases are completely decoupled from one another.

The company has a maximum budget $B$ for the total cancellation penalties. Determine if it is possible to achieve this segregation without the total penalty of the canceled initiatives exceeding $B$. If it is possible, provide a valid set of initiatives to cancel. (While it may be cheap to separate any specific pair of power bases, the budget must cover separating all of them from one another simultaneously.)

## Input
Line 1: four integers $n$, $m$, $k$, and $B$.
Line 2: $k$ distinct integers: the IDs of the departments designated as power bases.
Next $m$ lines: three integers $u$, $v$, and $w$ — a joint initiative between department $u$ and department $v$ with a cancellation penalty of $w$. Departments are numbered 1 to $n$.

## Output
`YES`, then a line with the number $c$ of canceled initiatives, then $c$ lines "$u$ $v$"; or `NO`. If there are multiple valid sets of initiatives to cancel within budget, any one is acceptable.

## Example

**Input**
```text
5 6 3 15
1 3 5
1 2 4
2 3 5
3 4 2
4 5 3
5 1 6
2 4 1
```

**Output**
```text
YES
4
1 2
5 1
3 4
2 4
```
