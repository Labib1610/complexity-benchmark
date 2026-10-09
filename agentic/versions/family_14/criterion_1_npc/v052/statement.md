# Problem A — Facility Data Exchange

Time limit: 5 s   Memory limit: 256 MB

## Description

A logistics company operates $n$ facilities, numbered 1 through $n$. Following an acquisition, they must configure a data exchange system so that $t$ mandatory facilities are fully integrated. 

A telecommunications provider offers $m$ potential bidirectional data bridges. Each bridge is established between exactly two facilities and requires a specific monthly activation fee. The company may choose to activate any subset of these bridges.

Data transmission across the system is governed entirely by these operational rules:
- If a bridge between facility $A$ and facility $B$ is activated, data can be transmitted from $A$ to $B$, and from $B$ to $A$.
- If data can be transmitted from facility $A$ to facility $C$, and from facility $C$ to facility $B$, then data can be transmitted from $A$ to $B$.

The company can activate bridges between any facilities, including those that are not mandatory, if doing so results in a cheaper overall configuration. The system is considered valid if, under the rules above, data can be successfully transmitted from every mandatory facility to every other mandatory facility. 

Determine the minimum total monthly activation fee required to achieve a valid system.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le 10$, $1 \le n \le 100$, $0 \le m \le n(n-1)/2$).
The second line contains $t$ distinct integers representing the IDs of the mandatory facilities.
Each of the following $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \ne v$, $1 \le w \le 1000000$), meaning that a bidirectional data bridge between facility $u$ and facility $v$ can be activated for a monthly fee of $w$.
It is guaranteed that activating all available bridges would create a valid system.

## Output

Print a single integer: the minimum total monthly activation fee required to create a valid system.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, activating the bridges between (1,4), (2,4), and (3,4) incurs a total fee of 1 + 1 + 1 = 3. Because data can be transmitted between any two of the mandatory facilities (1, 2, and 3) by utilizing the non-mandatory facility 4 as an intermediate step, this configuration is valid. It is cheaper than activating bridges directly between the mandatory facilities (which would cost 4). In Example 3, there is only one mandatory facility, so the condition is trivially fulfilled with no activated bridges.
