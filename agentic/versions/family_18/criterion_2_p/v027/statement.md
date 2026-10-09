# Problem B — Departmental Relocation

Time limit: 5 s   Memory limit: 256 MB

## Description
A team of $n$ researchers will be moving into a single hallway containing exactly $n$ distinct offices. The offices are arranged in a straight line and numbered sequentially from $1$ to $n$. Each researcher must be assigned to exactly one office, with no offices left empty.

Certain pairs of researchers work together on joint projects. You are given a list of $m$ such projects, each specifying two researchers who collaborate. The collaborations form a minimally integrated structure: all researchers are linked into a single overarching group, but there are no closed loops of joint projects.

When two collaborating researchers are assigned to their respective offices, the communication friction for their project is defined as the physical distance between them, calculated as the absolute difference between their assigned office numbers. The total friction for the entire department is the sum of the communication frictions across all $m$ joint projects.

The department has established a strict maximum friction limit, denoted by $B$. Your objective is to determine if there exists an assignment of researchers to offices such that the total friction is at most $B$. If such an assignment exists, you must also provide a valid office configuration.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of researchers, the number of joint projects, and the maximum allowed total friction. (You are guaranteed that $m = n - 1$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that researcher $u$ and researcher $v$ collaborate on a joint project. 

## Output
If the limit can be met, print `YES` on the first line. On the second line, print $n$ space-separated integers representing the assigned office numbers (from $1$ to $n$) for researcher 1, researcher 2, ..., up to researcher $n$. 
If it is impossible to meet the limit, print `NO`.

## Example

### Input
```text
5 4 6
1 3
2 3
3 4
3 5
```

### Output
```text
YES
1 2 3 4 5
```
