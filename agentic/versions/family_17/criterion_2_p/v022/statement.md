# Complete Disjoint Selection

Time limit: 2 s
Memory limit: 256 MB

## Description
In complex distributed systems, selecting a valid subset of configuration states from a vast combinatorial space is a difficult challenge. The state space of possible configurations grows drastically with the number of allowed connections.

You are given a system with $2q$ distinct subsystems. The subsystems are divided into two equal-sized blocks: $q$ primary subsystems (numbered $1$ through $q$) and $q$ secondary subsystems (numbered $q+1$ through $2q$).

You are also provided with a list of $t$ potential synchronization links. Each link connects exactly two subsystems. Because of architectural constraints, every available link connects exactly one primary subsystem and exactly one secondary subsystem.

A complete disjoint selection is a subset of these links chosen such that every subsystem (both primary and secondary) is included in exactly one chosen link. If a subsystem is left out, the system remains unsynchronized; if a subsystem is included in more than one chosen link, the interference causes a critical failure.

With $t$ up to 400,000, there are $2^t$ possible subsets, rendering naive exhaustive search impossible. Your task is to determine whether there exists at least one subset of links that forms a complete disjoint selection of all $2q$ subsystems. If such a subset exists, you must output it.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of primary subsystems (which is also the number of secondary subsystems) and the number of available synchronization links, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that a synchronization link is available between primary subsystem $a$ and secondary subsystem $b$.

## Output
If a complete disjoint selection is possible, print `YES` on the first line. Then, print $q$ lines, each containing the two subsystems of a chosen link in the selection. If multiple valid selections exist, you may output any of them. If no such selection is possible, print `NO`.

## Example

### Input
```text
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```text
YES
1 4
2 6
3 5
```
