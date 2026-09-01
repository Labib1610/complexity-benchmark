# Quantum Entanglement Relays

Time limit: 1 s   Memory limit: 256 MB

A quantum communication network consists of $n$ relay nodes, numbered $1$ through $n$. You must configure each relay to operate in one of two spin configurations, denoted by integer values $1$ and $2$.

The network's coherence is maintained by $m$ entanglement links. Each link connects a specific pair of relays. For a link to achieve quantum coherence and function correctly, the bitwise XOR of the integer values representing the spin configurations of the two connected relays must evaluate to exactly 3. If the bitwise XOR evaluates to any other value, the link collapses and yields an invalid state.

Your task is to assign a spin configuration (either $1$ or $2$) to each of the $n$ relays so that every entanglement link in the network operates correctly. If multiple valid assignments are possible, you must output the lexicographically smallest valid configuration (assigning configuration $1$ to lower-numbered relays whenever possible). If no such assignment is possible, you must report that it cannot be done.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing the indices of a pair of relays connected by an entanglement link.

## Output
If it is impossible to configure the relays to satisfy all links, output a single line with NO.
If it is possible, output YES on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1,2\}$) giving the lexicographically smallest valid configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```