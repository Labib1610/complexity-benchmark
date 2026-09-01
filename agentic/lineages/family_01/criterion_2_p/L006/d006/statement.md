# Orbital Reflection Synchrony

Time limit: 1 s   Memory limit: 256 MB

A satellite network consists of $n$ orbital modules, numbered $1$ through $n$. You must assign each module an operating mode, represented by the integer $1$ or $2$.

The modes determine how a module transforms an incoming diagnostic signal. A signal can be in one of four states, denoted by integers $1$ through $4$.
- Mode 1 transforms the signal state according to the mapping $M_1$: state 1 becomes 2, state 2 becomes 1, state 3 becomes 4, and state 4 becomes 3.
- Mode 2 transforms the signal state according to the mapping $M_2$: state 1 becomes 3, state 2 becomes 4, state 3 becomes 1, and state 4 becomes 2.

The network's synchronization is governed by $m$ telemetry channels. Each channel connects a specific pair of modules. For a channel to function correctly, the combined effect of the two modules' transformations on any signal must exactly match a specific target mapping $M_{target}$, which maps state 1 to 4, state 2 to 3, state 3 to 2, and state 4 to 1. 

That is, if you take any initial signal state $x \in \{1, 2, 3, 4\}$, apply the transformation for the mode assigned to one module, and then apply the transformation for the mode assigned to the other module, the final state must always be $M_{target}(x)$. (Since the mappings $M_1$ and $M_2$ commute, the order in which the two modules process the signal does not matter). If the combined transformations yield any other result for any state, the channel fails.

Your task is to assign an operating mode ($1$ or $2$) to each of the $n$ modules so that every telemetry channel functions correctly. If multiple valid assignments are possible, you must output the lexicographically smallest valid sequence of modes. If no such assignment is possible, you must report that it cannot be done.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), representing the indices of a pair of modules connected by a telemetry channel.

## Output
If it is impossible to configure the modules to satisfy all channels, output a single line with NO.
If it is possible, output YES on the first line. On the second line, output $n$ integers $p_1 \dots p_n$ (where each $p_i \in \{1,2\}$) giving the lexicographically smallest valid sequence of modes.

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