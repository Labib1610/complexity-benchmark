# Deep-Space Outpost Integration

Time limit: 2 s   Memory limit: 256 MB

## Description
A deep-space outpost is constructed from a total of $2q$ prefabricated units. Each unit is assigned a unique tracking integer from $1$ up to $2q$.

The outpost's blueprint mandates that the units be combined into self-sufficient pairs. Due to strict thermal management protocols, every pair must consist of exactly one energy generator (which are assigned the integers $1$ through $q$) and exactly one living quarters unit (which are assigned the integers from $q+1$ to $2q$).

Two units can only be linked if they share a certified interface. The engineering database contains $t$ such certified interoperability records. 

Your task is to organize all $2q$ units into valid pairs such that every single unit is utilized exactly once. 

You must establish if a full integration is achievable using only the certified records. If successful, output the pairs of units that will be linked; if it cannot be done, report that the integration is impossible.

## Input
The first line provides two integers $q$ and $t$. The outpost's central core has a maximum capacity of $100,000$ energy generators, so $q$ is a positive integer no greater than this maximum capacity. The engineering database can store up to $400,000$ interoperability records, meaning $t$ is a non-negative integer up to this storage limit.

This is followed by $t$ lines, each containing two integers $a$ and $b$. These represent a certified interface between an energy generator $a$ (a value from $1$ to $q$ inclusive) and a living quarters unit $b$ (a value from $q+1$ to $2q$ inclusive).

## Output
If a full integration is achievable, print `YES` on the first line. Following this, print $q$ lines, each providing the two tracking integers of a linked pair. If a full integration cannot be done, print `NO`.

## Example

**Input**
```text
3 5
1 4
1 5
2 5
3 5
3 6
```

**Output**
```text
YES
1 4
2 5
3 6
```
