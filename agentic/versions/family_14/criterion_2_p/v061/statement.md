# Problem B — Powering the Essential Units

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a distributed computing cluster consisting of $n$ processing units, numbered $1$ to $n$. You are given a blueprint of $m$ bidirectional data buses that can be activated. Each bus links two units and requires a specific amount of power to activate.

The blueprint follows a strict routing design: a signal sent from any unit to any other unit has exactly one sequence of buses it can follow. Because there are no alternate routes, the total number of buses $m$ in the blueprint is exactly $n - 1$.

A subset of $t$ units are designated as **essential**. Your task is to activate a subset of the available data buses such that all essential units can communicate with each other (either directly or by relaying signals through other units). Non-essential units may also be used as relays if needed.

Determine the minimum total power required to activate a valid subset of buses.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers: the IDs of the essential units.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1000000$), representing a data bus in the blueprint between unit $u$ and unit $v$ with an activation power of $w$. The blueprint satisfies the routing design described above.

## Output

Print a single integer: the minimum total power required to ensure all essential units can communicate.

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

In Example 1, essential units 1 and 4 can only communicate by routing through units 2 and 3, so all three buses (5 + 1 + 2 = 8) must be activated. In Example 2, there is only one essential unit, so no buses need to be activated.
