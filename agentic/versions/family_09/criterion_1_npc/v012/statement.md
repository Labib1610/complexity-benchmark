# Problem A — Diverse Focus Group

Time limit: 5 s
Memory limit: 256 MB

## Description

A social platform has $n$ users, numbered 1 through $n$, and $m$ direct communication links. Each link allows two specific users to interact.

You have been tasked with assembling a focus group of exactly $k$ users. To ensure that the group represents truly uninfluenced viewpoints, the selection must operate under the following restriction: whenever a user is chosen for the focus group, every other user who shares a communication link with them becomes strictly ineligible to be included in the same group.

You must determine whether it is possible to successfully select a focus group of exactly $k$ users that satisfies this restriction, and if so, provide a valid selection.

## Input

The first line contains three integers $n$, $m$, and $k$ ($1 \le n \le 46$, $0 \le m \le n(n-1)/2$, $1 \le k \le n$).
Each of the following $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a communication link between user $u$ and user $v$. No communication link is provided more than once.

## Output

If a valid focus group of $k$ users can be formed, output `YES` on the first line. On the second line, output $k$ distinct integers representing the user numbers in the focus group, separated by spaces. If there are multiple valid groups, you may output any of them.

If no such focus group can be formed, output `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```
