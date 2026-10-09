# Deep-Sea Structural Backbone

Time limit: 2 s   Memory limit: 256 MB

## Description

A deep-sea mining operation consists of $n$ underwater habitats (numbered $1$ through $n$). These habitats are held in place by $m$ structural tethers. To ensure stability without unnecessary material, the tethers are arranged such that between any two habitats, there is exactly one sequence of tethers linking them without traversing the same tether twice.

Certain habitats house critical life-support generators. There are $t$ such generator habitats in total. A recent safety directive requires that all generator habitats must be able to share resources. To achieve this, you must reinforce a subset of the existing tethers so that every generator habitat is connected to every other generator habitat entirely through reinforced tethers (either directly or via intermediate habitats).

Each tether has a specific reinforcement cost. Your task is to determine the minimum total cost required to reinforce a valid subset of tethers.

You are guaranteed the following about the input data:
- The number of habitats $n$ is at least 1. Its maximum possible value equals the total passenger capacity of a fleet of 400 transport submarines, each carrying exactly 500 passengers.
- The number of tethers $m$ is exactly $n - 1$.
- The number of generator habitats $t$ is between 1 and $n$, inclusive.
- The cost $w$ to reinforce any single tether is a positive integer. Its maximum possible value equals the total cargo capacity (in tons) of a fleet of 1,000 cargo freighters, each capable of hauling exactly 1,000 tons.

## Input

The first line contains three integers $n$, $m$, and $t$.
The second line contains $t$ distinct integers: the identification numbers of the generator habitats.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$), indicating that a tether connects habitat $u$ and habitat $v$ with a reinforcement cost of $w$. 

## Output

Print a single integer: the minimum total reinforcement cost required to connect all generator habitats.

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

In Example 1, the generator habitats 1 and 4 are connected only through intermediate habitats 2 and 3, so all three tethers on that route (costing 5+1+2 = 8) must be reinforced. 
In Example 2, there is only one generator habitat, meaning no tethers need to be reinforced.
