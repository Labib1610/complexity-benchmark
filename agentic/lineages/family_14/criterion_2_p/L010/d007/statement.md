# State Synchronization Licensing

Time limit: 2 s   Memory limit: 256 MB

## Description

A distributed computing cluster consists of $n$ independent data registers, numbered $1$ to $n$. You are provided a list of $m$ optional synchronization protocols. Each protocol continuously synchronizes register $u$ and register $v$ so that they unconditionally hold the same data state, and requires a one-time licensing fee of $w$ to activate.

The cluster's architecture guarantees that if you were to activate all $m$ protocols, all $n$ registers would be forced into a single uniform data state. The total number of available protocols $m$ is exactly $n - 1$.

A specific subset of $t$ registers are designated as critical. 

You must select a subset of the protocols to activate such that all $t$ critical registers are guaranteed to share the exact same data state, purely through the direct and transitive effects of the activated protocols. 

Your objective is to determine the minimum possible total licensing fee required to activate a valid set of protocols. (If there is only one critical register, no synchronization between multiple registers is needed, and the fee is zero).

## Input

The first line provides three integers: $n$, $m$, and $t$. The cluster supports up to two hundred thousand registers ($1 \le n \le 200000$). The number of available protocols $m$ is always exactly $n - 1$. The number of critical registers $t$ can range from a single register up to the entire cluster ($1 \le t \le n$).

The second line contains $t$ distinct integers representing the IDs of the critical registers.

Following this, there are $m$ lines, each detailing a single synchronization protocol with three integers: $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$). The one-time licensing fee $w$ for activating any single protocol is at least one and does not exceed one million units ($1 \le w \le 1000000$).

## Output

Print a single integer: the minimum possible total licensing fee required to activate a set of protocols such that all critical registers share the same data state.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the critical registers are 1 and 4. To ensure register 1 and register 4 share the same data state, the protocols between 1 and 2 (fee 5), 2 and 3 (fee 1), and 3 and 4 (fee 2) must be activated. The total fee is 5 + 1 + 2 = 8. This is the minimum possible total fee.

In Example 2, there is only one critical register (register 3). Since no synchronization between multiple critical registers is required, zero protocols need to be activated. The minimum possible total fee is 0.