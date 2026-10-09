# Problem B — Disconnected Assembly

Time limit: 2 s   Memory limit: 256 MB

## Description

You are evaluating a system made up of **n** components, which are identified by integers from 1 to **n**. Within this system, there are **m** bidirectional interference links. When two components share a link, they interfere with one another and cannot operate simultaneously.

The network of links possesses a specific underlying property: there exists at least one way to configure every component with a non-zero real-valued voltage such that, across every interference link, the voltages of the two connected components sum to exactly zero. You are not provided with these voltages; you only have the guarantee that such a configuration is mathematically possible.

Your objective is to find a **safe** subset of components. A subset is considered safe if it contains absolutely no interference links between any of its members.

Given a required subset size **k**, determine if a safe subset of exactly **k** components can be formed. If it can, output one such valid subset.

## Input

The first line provides three integers: **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Following this are **m** lines, each containing two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing an interference link between component **u** and component **v**. It is guaranteed that no link appears more than once, and that the entire network adheres to the voltage cancellation property described.

## Output

If it is possible to select exactly **k** components that form a safe subset, output `YES` on the first line. On the second line, output the **k** distinct component identifiers of your chosen subset, separated by single spaces. If multiple safe subsets of size **k** exist, any valid one will be accepted.

If no such subset can be formed, output `NO` on a single line.

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

In Example 1, components 1 and 2 do not share an interference link, so they can form a safe subset of size 2. In Example 3, the largest possible safe subset has only 2 components, making a subset of size 3 impossible.