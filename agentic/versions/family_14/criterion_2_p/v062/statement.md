# Problem B — Optimal Synchronization State

Time limit: 2 s
Memory limit: 256 MB

## Description
In a distributed processing environment, you are tasked with determining the optimal configuration for a network of $n$ modules. You are provided with a list of $m$ potential bidirectional synchronization channels. Each channel has an associated energy cost to power on.

A network configuration is defined by a boolean assignment to each of the $m$ channels, placing it in either a powered or unpowered state. With each channel configured independently, the configuration space contains $2^m$ distinct states. 

A subset of $t$ modules are designated as *critical*. A configuration is considered *valid* if all critical modules are able to exchange data with one another. Data exchange can occur directly between two modules via a powered channel, or indirectly by relaying through a sequence of powered channels (intermediate modules in the sequence do not need to be critical). 

Your objective is to evaluate the configuration space and find a valid configuration that minimizes the total energy cost of the powered channels. 

The physical layout of the environment is constrained such that there are exactly $m = n - 1$ potential channels. The cabling topology guarantees that in the specific configuration where all $m$ channels are powered, any two modules in the network are connected by exactly one sequence of distinct channels.

## Input
The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$, $m = n - 1$).
The second line contains $t$ distinct integers representing the identifiers of the critical modules.
Each of the following $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), indicating that a potential channel exists between module $u$ and module $v$ with an energy cost of $w$.

## Output
Print a single integer: the minimum total energy cost of a valid configuration.

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
