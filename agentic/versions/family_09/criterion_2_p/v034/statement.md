# Problem B — Stable Mixture (Even Chains)

Time limit: 2 s   Memory limit: 256 MB

## Description

A factory produces $n$ chemical compounds (identified by numbers 1 through $n$) and maintains a registry of $m$ reactive pairs. A reactive pair consists of two compounds that will cause an adverse reaction if mixed.

It is a fundamental property of this chemical system that if you trace any sequence of compounds starting and ending at the same compound, where each consecutive pair in the sequence is reactive, the total count of reactive pairs in that sequence is always an even number. 

A mixture of compounds is considered **stable** if no two compounds in the mixture are reactive with each other.

The factory's storage facility can hold a maximum of 100,000 distinct chemical compounds, and it currently holds $n$ of them (with at least a single compound present). The hazard registry is capable of documenting up to 400,000 reactive pairs, and currently lists $m$ such pairs (it is possible the registry is empty). You are tasked with selecting a target of exactly $k$ compounds (from a minimum of 1 up to the total $n$ available).

Given the target size $k$, decide whether a stable mixture of exactly $k$ compounds exists, and if so report one.

## Input

The first line contains three integers $n$, $m$, and $k$, bounded by the physical capacities and limits described above.
Each of the next $m$ lines contains two integers $u$ and $v$, representing the identifiers of a reactive pair. Compound identifiers are valid integers from 1 up to $n$. A compound is never reactive with itself ($u \neq v$). No reactive pair is listed more than once, and the interactions are guaranteed to follow the even-count sequence structure described above.

## Output

If a stable mixture of $k$ compounds exists, print `YES` on the first line, then on the second line print $k$ distinct compound identifiers forming such a mixture, separated by spaces. Any mixture in which no two compounds are reactive is accepted.

If no such mixture exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, compounds 1 and 2 do not react with each other and can form a stable mixture. In Example 3, the largest possible stable mixture consists of only 2 compounds, making a target of 3 impossible to achieve.
