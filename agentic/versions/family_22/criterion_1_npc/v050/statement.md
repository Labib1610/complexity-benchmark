# Problem A — Curating the Historical Hallway

Time limit: 5 s   Memory limit: 256 MB

## Description
A museum is organizing an exhibition of $n$ historical documents, numbered $1$ through $n$. The exhibition takes place in a long hallway that is divided into $T$ distinct sections. Visitors walk through these sections in a strict one-way path, starting at section $1$ and ending at section $T$.

Every document must be located in exactly one section. To ensure visitors have enough space to examine the pieces without crowding, the curators mandate that no section can hold more than $M$ documents.

To convey a coherent story, the curators have established $m$ narrative requirements. Each requirement specifies that a visitor must fully absorb the context of document $a$ before encountering document $b$. Because visitors might view items within the same section in any order, document $a$ must be located in a section that visitors reach strictly before the section housing document $b$. 

A strict limit on the number of documents per section can conflict with long sequences of narrative requirements. You must determine if there is a way to distribute all $n$ documents among the $T$ sections such that no section houses more than $M$ documents, and every narrative requirement is satisfied.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that document $a$ must be located in a section strictly before the section containing document $b$.

## Output
If a valid distribution is possible, print `YES` followed by a space-separated sequence of $n$ integers, where the $i$-th integer represents the section (from $1$ to $T$) where document $i$ is located. Otherwise, print `NO`.

## Example

### Input
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

### Output
```text
YES
1 1 2 3 3
```
