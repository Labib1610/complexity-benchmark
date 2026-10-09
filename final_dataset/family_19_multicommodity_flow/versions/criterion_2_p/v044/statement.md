# Problem B — Bounded Integer State Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
You are given a system of bounded variables representing a vast combinatorial state space. Specifically, you must assign an integer $x_j$ to each of $m$ directed channels that connect a network of $n$ junctions. Each channel $j$ has a strict upper bound $C_j$, meaning its assigned value must satisfy $0 \le x_j \le C_j$. The total number of possible assignments is the product of $(C_j + 1)$ across all channels, creating an astronomically large number of potential configurations.

Your objective is to find a single valid configuration of these integers that simultaneously satisfies a rigid system of linear equations. For every junction (with exactly two exceptions), the sum of the assigned values $x_j$ for all incoming channels must exactly equal the sum of the assigned values $x_j$ for all outgoing channels. Any deviation makes the entire configuration invalid.

The two exceptions are the injection junction $S$ and the extraction junction $T$. The system must be configured to process a target load of exactly $D$. At $S$, the total outgoing sum of assigned values minus the total incoming sum of assigned values must equal exactly $D$. Because all channels process identical, indistinguishable units of a single item type, there are no competing classes of variables to track in this system. Accordingly, at $T$, the total incoming sum of assigned values minus the total outgoing sum of assigned values must also equal exactly $D$.

Determine if there exists at least one valid configuration in the state space that satisfies all equations and bounds simultaneously, and if so, provide it.

## Input
Line 1: `n m 1` (where `n` is the number of junctions, `m` is the number of channels, and `1` is the number of item types).
Next line: `S T D` (injection junction, extraction junction, and target load).
Next `m` lines: `u v C` (a channel from junction `u` to junction `v` with upper bound `C`).

## Output
`YES` on the first line, then a second line with `m` integers representing the assigned value $x_j$ for each channel $j$ (in the same order the channels were given in the input); or `NO` if it is impossible.

## Example

**Input:**
```
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 5
```

**Output:**
```
YES
5 5 0 5 5
```
